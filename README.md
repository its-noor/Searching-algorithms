Grid-based Pathfinding Visualization
Overview
This repository contains implementations of various search algorithms for pathfinding in a grid-based world. The project demonstrates the use of common algorithms including:

Breadth-First Search (BFS)
Depth-First Search (DFS)
Greedy Best-First Search (GBFS)
A* Search
The algorithms are visualized using matplotlib, and the project is designed to work on a grid environment with obstacles (enclosures) and special areas (turfs) that affect traversal costs.

Project Structure
utils.py
Contains fundamental data structures such as Stack, Queue, and PriorityQueue that are used by the search algorithms.

grid.py
Provides the Point class and functions for drawing the grid, points, lines, and visualizing the search process.

search.py
Serves as the main driver script. It loads world data, sets up the grid visualization, and lets you choose which search algorithm to run.

Search Algorithm Implementations:

bfs.py: Implementation of Breadth-First Search.
dfs.py: Implementation of Depth-First Search.
gbfs.py: Implementation of Greedy Best-First Search.
astar.py: Implementation of A* Search.
World Files
The project expects world files that define the layout of obstacles (enclosures) and special traversal areas (turfs). These files are referenced in the code (in search.py) as:

TestingGrid/world1_enclosures.txt
TestingGrid/world1_turfs.txt
Note: The world files containing the polygon definitions for turfs and enclosures have not been added yet. You can either add your own world files following the required format or wait for an update when they are uploaded.

Expected World File Format
Each world file should include one polygon per line. Each polygon is defined as a series of x,y coordinates separated by semicolons (;). For example:

Copy
1,2;3,4;5,6;7,8
Each line represents a polygon, and the vertices are used to determine the boundaries of enclosures or turfs in the grid.

Requirements
Python 3.x
matplotlib
numpy
You can install the required packages using pip:

bash
Copy
pip install matplotlib numpy
How to Run
Execute the main script using:

bash
Copy
python search.py
After running the script, follow the on-screen prompt to select the desired search algorithm:

1: BFS
2: DFS
3: GBFS
4: A*
The script will display a grid, mark the source and destination, draw the obstacles (if provided), and animate the search process. If a valid path is found, it will be highlighted on the grid.

Contributing
Contributions, bug fixes, and enhancements are welcome! Please open issues or submit pull requests if you have suggestions or improvements.
