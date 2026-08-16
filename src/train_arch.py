"""
Training script for a single architecture on CIFAR-10 or CIFAR-100.
Returns training curves and final metrics.
"""

import time
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split


def get_cifar_loaders(dataset_name="cifar10", batch_size=128, val_split=0.1, seed=42):
    """Get CIFAR train/val/test loaders."""
    normalize = transforms.Normalize(
        mean=[0.4914, 0.4822, 0.4465],
        std=[0.2470, 0.2435, 0.2616],
    )

    train_transform = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        normalize,
    ])

    test_transform = transforms.Compose([
        transforms.ToTensor(),
        normalize,
    ])

    dataset_cls = torchvision.datasets.CIFAR10 if dataset_name == "cifar10" else torchvision.datasets.CIFAR100
    num_classes = 10 if dataset_name == "cifar10" else 100

    full_train = dataset_cls(root="./data", train=True, download=True, transform=train_transform)
    test_set = dataset_cls(root="./data", train=False, download=True, transform=test_transform)

    # Split train into train/val
    val_size = int(len(full_train) * val_split)
    train_size = len(full_train) - val_size
    generator = torch.Generator().manual_seed(seed)
    train_set, val_set = random_split(full_train, [train_size, val_size], generator=generator)

    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True,
                              num_workers=4, pin_memory=True, drop_last=True)
    val_loader = DataLoader(val_set, batch_size=batch_size, shuffle=False,
                            num_workers=4, pin_memory=True)
    test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False,
                             num_workers=4, pin_memory=True)

    return train_loader, val_loader, test_loader, num_classes


def train_architecture(model, dataset_name="cifar10", epochs=50, batch_size=128,
                       lr=0.1, weight_decay=5e-4, seed=42, device="cuda"):
    """Train a model on CIFAR and return detailed metrics."""
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    train_loader, val_loader, test_loader, num_classes = get_cifar_loaders(
        dataset_name, batch_size, seed=seed
    )

    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=weight_decay)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    scaler = torch.amp.GradScaler('cuda')

    history = {
        "train_loss": [],
        "val_loss": [],
        "train_acc": [],
        "val_acc": [],
        "epoch_time": [],
    }

    start_time = time.time()

    for epoch in range(epochs):
        epoch_start = time.time()

        # Training
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            optimizer.zero_grad()
            with torch.amp.autocast('cuda', dtype=torch.bfloat16):
                outputs = model(inputs)
                loss = criterion(outputs, targets)
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()

            running_loss += loss.item() * inputs.size(0)
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

        train_loss = running_loss / total
        train_acc = 100.0 * correct / total

        # Validation
        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0
        with torch.no_grad():
            for inputs, targets in val_loader:
                inputs, targets = inputs.to(device), targets.to(device)
                with torch.amp.autocast('cuda', dtype=torch.bfloat16):
                    outputs = model(inputs)
                    loss = criterion(outputs, targets)
                val_loss += loss.item() * inputs.size(0)
                _, predicted = outputs.max(1)
                total += targets.size(0)
                correct += predicted.eq(targets).sum().item()

        val_loss = val_loss / total
        val_acc = 100.0 * correct / total

        scheduler.step()
        epoch_time = time.time() - epoch_start

        history["train_loss"].append(round(train_loss, 4))
        history["val_loss"].append(round(val_loss, 4))
        history["train_acc"].append(round(train_acc, 2))
        history["val_acc"].append(round(val_acc, 2))
        history["epoch_time"].append(round(epoch_time, 2))

    # Final test evaluation
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, targets in test_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            with torch.amp.autocast('cuda', dtype=torch.bfloat16):
                outputs = model(inputs)
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

    test_acc = 100.0 * correct / total
    total_time = time.time() - start_time

    return {
        "test_acc": round(test_acc, 2),
        "best_val_acc": round(max(history["val_acc"]), 2),
        "final_train_acc": round(history["train_acc"][-1], 2),
        "final_val_acc": round(history["val_acc"][-1], 2),
        "train_val_gap": round(history["train_acc"][-1] - history["val_acc"][-1], 2),
        "total_time_s": round(total_time, 1),
        "history": history,
    }
