"""Dijkstra's algorithm on a weighted grid (Week 4).

Like BFS, but the frontier is a priority queue ordered by cost-so-far, so it
handles cells that cost more to enter. Guarantees a lowest-cost path.
"""

from __future__ import annotations

import heapq

from src.grid.grid import neighbors

def reconstruct_path(came_from, goal):
    if (goal not in came_from):
        return None
    path = []
    while goal != None:
        path.append(goal)
        goal = came_from[goal]
    return path[::-1]

def cost(grid, a, b):
    """Cost to move from cell a to neighbor b.

    Start with 1.0 for 4-connected moves. For 8-connected, diagonal moves
    should cost sqrt(2). You can extend this later for weighted terrain.
    """
    if a[0] != b[0] and a[1] != b[1]:
        return (2**0.5)
    return 1.0


def dijkstra(grid, start, goal, connectivity=4):
    """Find a lowest-cost path from start to goal.

    Return a list of cells, or None if unreachable.

    TODO (Week 4):
      - frontier = heapq of (cost_so_far, cell)
      - cost_so_far dict, came_from dict
      - relax neighbors: if new cost is cheaper, update and push
    """
    frontier = [(0, start)]
    cost_so_far = dict()
    came_from = dict()
    cost_so_far[start] = 0
    came_from[start] = None
    while (len(frontier) > 0) and (goal not in came_from):
        currentCost, currentCell = heapq.heappop(frontier)
        if currentCost != cost_so_far[currentCell]:
            continue
        for neighborCell in neighbors(grid, currentCell, connectivity):
            newCost = currentCost + cost(grid, currentCell, neighborCell)
            if (neighborCell in came_from) and cost_so_far[neighborCell] <= newCost:
                continue
            came_from[neighborCell] = currentCell
            cost_so_far[neighborCell] = newCost
            heapq.heappush(frontier, (newCost, neighborCell))
    return reconstruct_path(came_from, goal)
