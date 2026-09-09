"""Dijkstra's algorithm on a weighted grid (Week 4).

Like BFS, but the frontier is a priority queue ordered by cost-so-far, so it
handles cells that cost more to enter. Guarantees a lowest-cost path.
"""

from __future__ import annotations

import heapq

from src.grid.grid import neighbors


def cost(grid, a, b):
    """Cost to move from cell a to neighbor b.

    Start with 1.0 for 4-connected moves. For 8-connected, diagonal moves
    should cost sqrt(2). You can extend this later for weighted terrain.
    """
    return 1.0


def dijkstra(grid, start, goal, connectivity=4):
    """Find a lowest-cost path from start to goal.

    Return a list of cells, or None if unreachable.

    TODO (Week 4):
      - frontier = heapq of (cost_so_far, cell)
      - cost_so_far dict, came_from dict
      - relax neighbors: if new cost is cheaper, update and push
    """
    raise NotImplementedError("Week 4: implement dijkstra()")
