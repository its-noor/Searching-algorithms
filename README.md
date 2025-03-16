# Pathfinding Algorithms on Grid with Obstacles

## Overview
This project implements various pathfinding algorithms on a grid with obstacles, enclosures, and different terrain types. The algorithms navigate a 2D world while considering barriers and traversal costs.

## Algorithms Implemented
- **A** Search (Astar) - Uses heuristics for optimal pathfinding.
- **Breadth-First Search (BFS)** - Explores all neighbors level by level.
- **Depth-First Search (DFS)** - Explores deeper paths before backtracking.
- **Greedy Best-First Search (GBFS)** - Uses heuristics but does not guarantee an optimal path.

## Grid Representation
The grid is represented using the `grid.py` file, which provides:
- A **50x50 grid** for pathfinding.
- **Visualization utilities** using `matplotlib`.
- Functions to draw points, paths, and obstacles.

## World Data (Testing Grid)
The world contains obstacles categorized into:
1. **Enclosures** - Impassable barriers.
2. **Turfs** - Areas with higher traversal cost.

These are stored in text files inside the `TestingGrid/` directory:
- `world1_enclosures.txt` - Defines enclosed regions.
- `world1_turfs.txt` - Defines turfs affecting movement costs.

## Running the Program
Execute the main search script:
```bash
python search.py
```
Upon running, the program will prompt you to select a search algorithm, display the search path, and visualize the result.


## Here is what you should expect upon selecting an algorithm 
![Screenshot 2025-02-28 173926](https://github.com/user-attachments/assets/d39d74c3-b470-4baf-b0a4-2fbd58af314f)




## Dependencies
Ensure you have the required dependencies installed:
```bash
pip install matplotlib numpy
```

## Directory Structure
```
📂 TestingGrid
│   ├── world1_enclosures.txt
│   ├── world1_turfs.txt
│   ├── world2_enclosures.txt
│   ├── world2_turfs.txt
├── astar.py
├── bfs.py
├── dfs.py
├── gbfs.py
├── grid.py
├── search.py
├── utils.py
└── README.md
```

## Future Improvements
- Adding more world configurations.
- Implementing additional pathfinding algorithms.
- Improving visualization and performance optimizations.


