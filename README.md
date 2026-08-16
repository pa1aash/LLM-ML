# LLM-ML

A controlled study of architecture-generation strategies for small convolutional
networks.

## Layout

```
src/       experiment runners, training, analysis, and model-server code
scripts/   shell orchestrators for the experiment suite
paper/     LaTeX manuscript and figures
audit/     evidence audit of the manuscript against this repository
archive/   prior manuscript snapshots
```

## Requirements

PyTorch + torchvision, transformers, matplotlib. Experiments were run on cloud
GPU hosts; see the script headers for the invocation used.

## Status

Work in progress. Interfaces and results are subject to change.
