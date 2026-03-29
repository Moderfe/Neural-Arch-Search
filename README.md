# Neural-Arch-Search

A research-focused repository exploring efficient Neural Architecture Search (NAS) algorithms to automate the design of optimal deep learning models.

## Research Areas
- **Differentiable Architecture Search (DARTS)**: Continuous relaxation of the search space for faster convergence.
- **Reinforcement Learning for NAS**: Using Proximal Policy Optimization (PPO) to discover novel architectures.
- **Hardware-Aware NAS**: Optimizing models for specific hardware constraints (latency, memory, power).

## Key Features
- **Modular Search Space**: Easily define and modify search spaces for different tasks.
- **Performance Predictors**: Integrated surrogate models to estimate architecture performance without full training.
- **Visualization Tools**: Generate architecture diagrams and search progress plots.

## Getting Started
```python
from nas_lib import SearchEngine

# Define search space and start search
engine = SearchEngine(config='configs/hardware_aware.yaml')
best_arch = engine.search()

# Export discovered architecture
best_arch.save('models/optimized_vit.pth')
```

## Citation
If you use this code in your research, please cite:
```bibtex
@misc{sterling2024nas,
  author = {Marcus D. Sterling},
  title = {Neural-Arch-Search: Efficient Architecture Discovery},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/Moderfe/Neural-Arch-Search}}
}
```

## License
MIT License
