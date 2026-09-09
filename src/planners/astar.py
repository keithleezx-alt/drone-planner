"""A* search on a grid (Week 5).

A* = Dijkstra + a heuristic that estimates remaining distance to the goal.
The heuristic guides the search toward the goal, so A* expands far fewer
nodes than Dijkstra while still finding an optimal path (as long as the
heuristic never overestimates — i.e. it's "admissible").
"""

from __future__ import annotations

import heapq
import math

from src.grid.grid import neighbors
from src.planners.dijkstra import cost


def heuristic(a, b, connectivity=4):
    """Estimate the distance from a to b.

    TODO (Week 5):
      - 4-connected: Manhattan distance |dr| + |dc|
      - 8-connected: octile or Euclidean distance
    Keep it admissible (never larger than the true remaining cost).
    """
    raise NotImplementedError("Week 5: implement heuristic()")


def astar(grid, start, goal, connectivity=4):
    """Find an optimal path using A*.

    Return (path, nodes_expanded) so you can compare against Dijkstra.

    TODO (Week 5):
      - frontier = heapq of (f = g + h, cell)
      - track g (cost so far) and came_from
      - count how many nodes you pop/expand
    """
    raise NotImplementedError("Week 5: implement astar()")
