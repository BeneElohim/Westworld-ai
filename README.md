Westworld simulation game, optimized for integration with blockchain technology and development for the Unity and Unreal SDKs:

# Westworld Simulation Game

![Westworld Cover](docs/img/cover_hq_westworld1.jpg)

## Description
**Westworld UnityGridAI using Unity and Unreal SDKs** is a multi-agent simulation library designed to simulate and optimize complex systems and environments where multiple agents interact. Drawing inspiration from theo.alves.da.costa 2d westworld simulation.  Unity software and [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents), this library is adapted for Python to enhance flexibility and scalability.

Our goal is to simulate diverse environments such as logistics, retail, and epidemiology by providing pre-coded spatial environments and agent communication frameworks. The system includes optimization capabilities using heuristics and Reinforcement Learning techniques.

**Note: This library is highly experimental, currently under active development, and in its alpha release stage. Features may be incomplete or untested.** For inquiries, please contact us at ron.khan@unitygrid.ai 

*The name "Westworld" is inspired by the TV series, which portrays a sophisticated multi-agent simulation system.*

## Documentation
Comprehensive documentation is available in the `docs` folder or online at [Westworld Documentation](https://theolvs.github.io/westworld).

## Features

### Current Features
- **Flexible Environment Creation**: Supports both grid and non-grid environments.
- **Diverse Objects**: Includes agents, obstacles, collectibles, and triggers with easy subclassing for custom objects.
- **Random Object Spawner**: Generate objects randomly within the environment.
- **Basic Physics System**: Implements a simple rigid body system for all objects.
- **Agent Behaviors**: Features pathfinding, wandering, random walk, fleeing, and vision range behaviors.
- **Maze Generation**: Automatic generation of mazes.
- **Image-to-Grid Conversion**: Convert images to obstacles and align them to the grid.
- **Sample Simulations**: Includes sample agents and simulations for classic scenarios.
- **Simulation Tools**: Visualize, replay, and export simulations as GIFs or videos.

### Roadmap Features
- **Expanded Simulations and Tutorials**: Additional classic simulations like boids and sugarscape.
- **Enhanced Pathfinding**: Improved algorithms for agent navigation.
- **Reinforcement Learning Integration**: Seamless integration with Stable Baselines for reinforcement learning.
- **Advanced Visualization**: Alternative visualization tools beyond PyGame, including web integration.

## Installation

### Install from PyPi
Install the library directly from PyPi using:
```sh
pip install westworld
```

### Developer Setup
To contribute to the development, you can clone the GitHub repository and set up the environment using Poetry:

```sh
# Clone the repository
git clone https://github.com/theolvs/westworld.git

# Navigate to the project directory
cd westworld

# Install dependencies and set up the environment
poetry install

# Run Jupyter Notebook or a Python console
poetry run jupyter notebook
poetry run python
```

