"""Breadth-First Search on a grid (Week 4).

BFS explores the grid level by level. On an unweighted grid it finds the
shortest path in number of steps. This is your first search algorithm and the
foundation for Dijkstra and A*.
"""

from __future__ import annotations

from collections import deque

from src.grid.grid import neighbors


def bfs(grid, start, goal, connectivity=4):
    """Find a shortest path from start to goal using BFS.

    Return a list of cells [start, ..., goal], or None if no path exists.

    TODO (Week 4):
      - use a deque as the frontier (FIFO)
      - keep a `came_from` dict mapping each visited cell to the cell you
        reached it from (start maps to None)
      - when you pop the goal, reconstruct the path by walking came_from back
    Hint: write a small reconstruct_path(came_from, goal) helper — you'll reuse
    it in dijkstra and astar.
    """
    raise NotImplementedError("Week 4: implement bfs()")
