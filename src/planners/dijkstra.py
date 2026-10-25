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

def reconstruct_path(came_from, goal):
  path=[]
  current=goal
  while current is not None:
    path.append(current)
    current=came_from[current]

  path.reverse()
  return path

def dijkstra(grid, start, goal, connectivity=4):
    """Find a lowest-cost path from start to goal.

    Return a list of cells, or None if unreachable.

    TODO (Week 4):
      - frontier = heapq of (cost_so_far, cell)
      - cost_so_far dict, came_from dict
      - relax neighbors: if new cost is cheaper, update and push
    """
  frontier=[]
  heapq.heappush(frontier,(0,start))
  came_from={start: None}
  cost_so_far={start:0}
  while frontier:
    current_cost, current=heapq.heappop(frontier)
    if current_cost>cost_so_far[current]:
      continue

    if current==goal:
      return reconstruct_path(came_from, goal)
    for next_cell in neighbors(grid, current, connectivity):
      new_cost=cost_so_far[current]+cost(grid, current, next_cell)

      if next_cell not in cost_so_far or new_cost< cost_so_far[next_cell]:
        cost_so_far[next_cell]=new_cost
        came_from[next_cell]=current
        heapq.heappush(frontier,(new_cost,next_cell))
  return None

  