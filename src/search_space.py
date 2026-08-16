"""
Search space definition for LLM-guided architecture design experiments.
Defines the modular CNN search space and random sampling.
"""

import random
import torch
import torch.nn as nn
import torch.nn.functional as F


# Search space configuration
SEARCH_SPACE = {
    "num_blocks": [3, 4, 5, 6],
    "conv_type": ["standard_3x3", "depthwise_separable", "dilated_3x3", "bottleneck"],
    "channels": [32, 64, 128, 256],
    "activation": ["relu", "gelu", "silu", "mish"],
    "normalization": ["batchnorm", "layernorm", "groupnorm", "none"],
    "skip_connection": ["identity", "projection", "none"],
    "pooling": ["maxpool", "avgpool", "strided_conv", "none"],
    "global_pool": ["avg", "max"],
    "fc_layers": [1, 2],
    "dropout": [0.0, 0.1, 0.3, 0.5],
}

MAX_PARAMS = 5_000_000


def get_activation(name):
    return {
        "relu": nn.ReLU(inplace=True),
        "gelu": nn.GELU(),
        "silu": nn.SiLU(inplace=True),
        "mish": nn.Mish(inplace=True),
    }[name]


def get_norm(name, channels):
    if name == "batchnorm":
        return nn.BatchNorm2d(channels)
    elif name == "layernorm":
        # Use GroupNorm(1, C) as a proxy for LayerNorm in conv layers
        return nn.GroupNorm(1, channels)
    elif name == "groupnorm":
        num_groups = min(32, channels)
        while channels % num_groups != 0:
            num_groups -= 1
        return nn.GroupNorm(num_groups, channels)
    elif name == "none":
        return nn.Identity()


class StandardConv(nn.Module):
    def __init__(self, in_c, out_c):
        super().__init__()
        self.conv = nn.Conv2d(in_c, out_c, 3, padding=1, bias=False)

    def forward(self, x):
        return self.conv(x)


class DepthwiseSeparableConv(nn.Module):
    def __init__(self, in_c, out_c):
        super().__init__()
        self.depthwise = nn.Conv2d(in_c, in_c, 3, padding=1, groups=in_c, bias=False)
        self.pointwise = nn.Conv2d(in_c, out_c, 1, bias=False)

    def forward(self, x):
        return self.pointwise(self.depthwise(x))


class DilatedConv(nn.Module):
    def __init__(self, in_c, out_c):
        super().__init__()
        self.conv = nn.Conv2d(in_c, out_c, 3, padding=2, dilation=2, bias=False)

    def forward(self, x):
        return self.conv(x)


class BottleneckConv(nn.Module):
    def __init__(self, in_c, out_c):
        super().__init__()
        mid_c = max(in_c // 4, 16)
        self.conv1 = nn.Conv2d(in_c, mid_c, 1, bias=False)
        self.conv2 = nn.Conv2d(mid_c, mid_c, 3, padding=1, bias=False)
        self.conv3 = nn.Conv2d(mid_c, out_c, 1, bias=False)

    def forward(self, x):
        return self.conv3(self.conv2(self.conv1(x)))


def get_conv(conv_type, in_c, out_c):
    return {
        "standard_3x3": StandardConv,
        "depthwise_separable": DepthwiseSeparableConv,
        "dilated_3x3": DilatedConv,
        "bottleneck": BottleneckConv,
    }[conv_type](in_c, out_c)


class Block(nn.Module):
    def __init__(self, in_c, out_c, conv_type, activation, normalization, skip_connection, pooling):
        super().__init__()
        self.conv = get_conv(conv_type, in_c, out_c)
        self.norm = get_norm(normalization, out_c)
        self.act = get_activation(activation)

        self.skip_type = skip_connection
        if skip_connection == "identity" and in_c == out_c:
            self.skip = nn.Identity()
        elif skip_connection == "projection" or (skip_connection == "identity" and in_c != out_c):
            self.skip = nn.Conv2d(in_c, out_c, 1, bias=False)
        else:
            self.skip = None

        self.pool_type = pooling
        if pooling == "maxpool":
            self.pool = nn.MaxPool2d(2)
        elif pooling == "avgpool":
            self.pool = nn.AvgPool2d(2)
        elif pooling == "strided_conv":
            self.pool = nn.Conv2d(out_c, out_c, 3, stride=2, padding=1, bias=False)
        else:
            self.pool = None

    def forward(self, x):
        out = self.act(self.norm(self.conv(x)))
        if self.skip is not None:
            out = out + self.skip(x)
        if self.pool is not None:
            out = self.pool(out)
        return out


class SearchableNetwork(nn.Module):
    def __init__(self, config, num_classes=10, input_channels=3):
        super().__init__()
        self.config = config

        # Initial stem
        first_channels = config["blocks"][0]["channels"]
        self.stem = nn.Sequential(
            nn.Conv2d(input_channels, first_channels, 3, padding=1, bias=False),
            nn.BatchNorm2d(first_channels),
            nn.ReLU(inplace=True),
        )

        # Build blocks
        blocks = []
        in_c = first_channels
        for block_cfg in config["blocks"]:
            out_c = block_cfg["channels"]
            blocks.append(Block(
                in_c, out_c,
                block_cfg["conv_type"],
                block_cfg["activation"],
                block_cfg["normalization"],
                block_cfg["skip_connection"],
                block_cfg["pooling"],
            ))
            in_c = out_c
        self.blocks = nn.Sequential(*blocks)

        # Global pooling
        if config["global_pool"] == "avg":
            self.global_pool = nn.AdaptiveAvgPool2d(1)
        else:
            self.global_pool = nn.AdaptiveMaxPool2d(1)

        # Classifier head
        fc_layers = []
        fc_in = in_c
        if config["fc_layers"] == 2:
            fc_layers.append(nn.Linear(fc_in, 256))
            fc_layers.append(nn.ReLU(inplace=True))
            if config["dropout"] > 0:
                fc_layers.append(nn.Dropout(config["dropout"]))
            fc_in = 256
        fc_layers.append(nn.Linear(fc_in, num_classes))
        self.classifier = nn.Sequential(*fc_layers)

    def forward(self, x):
        x = self.stem(x)
        x = self.blocks(x)
        x = self.global_pool(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x


def random_architecture_config(rng=None):
    """Sample a random architecture configuration from the search space."""
    if rng is None:
        rng = random

    num_blocks = rng.choice(SEARCH_SPACE["num_blocks"])

    # Decide how many pooling layers (can't pool more times than spatial dims allow)
    # CIFAR is 32x32, so max 4 pooling operations (down to 2x2)
    max_pools = min(num_blocks, 4)
    num_pools = rng.randint(1, max_pools)
    # Distribute pooling across blocks
    pool_positions = sorted(rng.sample(range(num_blocks), num_pools))

    blocks = []
    for i in range(num_blocks):
        pooling = rng.choice(["maxpool", "avgpool", "strided_conv"]) if i in pool_positions else "none"
        blocks.append({
            "conv_type": rng.choice(SEARCH_SPACE["conv_type"]),
            "channels": rng.choice(SEARCH_SPACE["channels"]),
            "activation": rng.choice(SEARCH_SPACE["activation"]),
            "normalization": rng.choice(SEARCH_SPACE["normalization"]),
            "skip_connection": rng.choice(SEARCH_SPACE["skip_connection"]),
            "pooling": pooling,
        })

    config = {
        "blocks": blocks,
        "global_pool": rng.choice(SEARCH_SPACE["global_pool"]),
        "fc_layers": rng.choice(SEARCH_SPACE["fc_layers"]),
        "dropout": rng.choice(SEARCH_SPACE["dropout"]),
    }
    return config


def config_to_string(config):
    """Convert config to a compact human-readable string."""
    parts = []
    for i, b in enumerate(config["blocks"]):
        pool_str = f"+{b['pooling']}" if b["pooling"] != "none" else ""
        skip_str = f"+skip_{b['skip_connection']}" if b["skip_connection"] != "none" else ""
        parts.append(f"B{i}({b['conv_type']},{b['channels']},{b['activation']},{b['normalization']}{skip_str}{pool_str})")
    head = f"Head(pool={config['global_pool']},fc={config['fc_layers']},drop={config['dropout']})"
    return " -> ".join(parts) + " -> " + head


def count_parameters(model):
    return sum(p.numel() for p in model.parameters())


def build_and_validate(config, num_classes=10):
    """Build a network from config and validate it.
    Returns (model, param_count) or (None, reason_string) if invalid."""
    try:
        model = SearchableNetwork(config, num_classes=num_classes)
        param_count = count_parameters(model)
        if param_count > MAX_PARAMS:
            return None, f"Too many parameters: {param_count:,} > {MAX_PARAMS:,}"

        # Test forward pass
        x = torch.randn(2, 3, 32, 32)
        with torch.no_grad():
            out = model(x)
        if out.shape != (2, num_classes):
            return None, f"Wrong output shape: {out.shape}, expected (2, {num_classes})"

        return model, param_count
    except Exception as e:
        return None, f"Build error: {str(e)}"


SEARCH_SPACE_DESCRIPTION = """
## Neural Architecture Search Space

Design a CNN architecture for image classification on CIFAR (32x32 RGB images).

### Architecture Template
The network consists of:
1. **Stem**: Fixed Conv2d(3, first_block_channels, 3) + BatchNorm + ReLU
2. **K Blocks** (K ∈ {3, 4, 5, 6}), each containing:
   - **Convolution type**: standard_3x3, depthwise_separable, dilated_3x3, or bottleneck (1x1→3x3→1x1)
   - **Output channels**: 32, 64, 128, or 256
   - **Activation**: relu, gelu, silu, or mish
   - **Normalization**: batchnorm, layernorm, groupnorm, or none
   - **Skip connection**: identity (if channels match), projection (1x1 conv), or none
   - **Pooling**: maxpool, avgpool, strided_conv, or none (spatial downsampling by 2x)
3. **Global pooling**: avg or max
4. **Classifier head**: 1 or 2 FC layers, with dropout ∈ {0, 0.1, 0.3, 0.5}

### Constraints
- Total parameters must be ≤ 5,000,000
- Input: 32×32×3 (CIFAR images)
- At least 1 and at most 4 pooling operations (CIFAR is 32×32)

### Output Format
Return a JSON configuration with this exact structure:
```json
{
  "blocks": [
    {
      "conv_type": "standard_3x3",
      "channels": 64,
      "activation": "relu",
      "normalization": "batchnorm",
      "skip_connection": "projection",
      "pooling": "none"
    },
    ...
  ],
  "global_pool": "avg",
  "fc_layers": 1,
  "dropout": 0.1
}
```

Valid values for each field:
- conv_type: "standard_3x3", "depthwise_separable", "dilated_3x3", "bottleneck"
- channels: 32, 64, 128, 256
- activation: "relu", "gelu", "silu", "mish"
- normalization: "batchnorm", "layernorm", "groupnorm", "none"
- skip_connection: "identity", "projection", "none"
- pooling: "maxpool", "avgpool", "strided_conv", "none"
- global_pool: "avg", "max"
- fc_layers: 1, 2
- dropout: 0.0, 0.1, 0.3, 0.5
"""
