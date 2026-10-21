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
from src.planners.dijkstra import reconstruct_path


def heuristic(a, b, connectivity=4):
    """Estimate the distance from a to b.

    TODO (Week 5):
      - 4-connected: Manhattan distance |dr| + |dc|
      - 8-connected: octile or Euclidean distance
    Keep it admissible (never larger than the true remaining cost).
    """
    deltaRow = abs(a[0] - b[0])
    deltaCol = abs(a[1] - b[1])
    if connectivity == 4:
        deltaRow + deltaCol
    return min(deltaRow, deltaCol) * (2 ** 0.5) + abs(deltaRow - deltaCol)


def astar(grid, start, goal, connectivity=4):
    """Find an optimal path using A*.

    Return (path, nodes_expanded) so you can compare against Dijkstra.

    TODO (Week 5):
      - frontier = heapq of (f = g + h, cell)
      - track g (cost so far) and came_from
      - count how many nodes you pop/expand
    """
    expandedNodes = 0
    frontier = [(heuristic(start, goal), start)]
    cost_so_far = dict()
    came_from = dict()
    cost_so_far[start] = 0
    came_from[start] = None
    while (len(frontier) > 0) and (goal not in came_from):
        expandedNodes += 1
        currentCost, currentCell = heapq.heappop(frontier)
        currentCost -= heuristic(currentCell, goal)
        if currentCost != cost_so_far[currentCell]:
            continue
        for neighborCell in neighbors(grid, currentCell, connectivity):
            newCost = currentCost + cost(grid, currentCell, neighborCell)
            if (neighborCell in came_from) and cost_so_far[neighborCell] <= newCost:
                continue
            came_from[neighborCell] = currentCell
            cost_so_far[neighborCell] = newCost
            heapq.heappush(frontier, (newCost + heuristic(neighborCell, goal), neighborCell))
    return (reconstruct_path(came_from, goal), expandedNodes)
