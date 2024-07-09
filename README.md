# Bloxorz AI

This repository contains AI solutions for the Bloxorz game using two methods: Depth-First Search (DFS) and A* (AStar) algorithms.

## Overview

The AI can find solutions to Bloxorz maps without gates. The data structures used include a tree for storing moves and a 2D linked list for map data. The tree setup and search methods are implemented recursively.

## Methods

### Depth-First Search (DFS)

The DFS method explores all possible paths in the search tree from the start position to the goal, backtracking when it encounters a dead end.

- **Directory:** `DFS/`
- **Implementation:** `dfs.py`

### A* (AStar)

The A* method uses a heuristic to guide the search, aiming to find the shortest path to the goal more efficiently than DFS.

- **Directory:** `AStar/`
- **Implementation:** `astar.py`

## Files

- `maze.py`: Contains the map data and related operations.
- `README.txt`: Brief description of the project and methods.

## Contribution

Feel free to contribute by forking the repository and submitting pull requests.

---

You can find the repository [here](https://github.com/berketonoz/bloxorz_ai).
