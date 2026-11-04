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



def heuristic(a, b, connectivity=4):
    """Estimate the distance from a to b.

    TODO (Week 5):
      - 4-connected: Manhattan distance |dr| + |dc|
      - 8-connected: octile or Euclidean distance
    Keep it admissible (never larger than the true remaining cost).
    """
    ar=a[0]
    ac=a[1]
    br=b[0]
    bc=b[1]
    if (connectivity==4):
      estdis=abs(ar-br)+abs(ac-bc)
    elif (connectivity==8):
      dr=abs(ar-br)
      dc=abs(ac-bc)
      estdis=min(dr,dc)* math.sqrt(2)+abs(dr-dc)
    return estdis

def cost(grid, a, b):
    ar=a[0]
    ac=a[1]
    br=b[0]
    bc=b[1]

    movecost=math.sqrt((ar-br)*(ar-br)+(ac-bc)*(ac-bc))
    return movecost


def reconstruct_path(came_from, goal):
  path=[]
  current=goal
  while current is not None:
    path.append(current)
    current=came_from[current]

  path.reverse()
  return path


def astar(grid, start, goal, connectivity=4):
    """Find an optimal path using A*.

    Return (path, nodes_expanded) so you can compare against Dijkstra.

    TODO (Week 5):
      - frontier = heapq of (f = g + h, cell)
      - track g (cost so far) and came_from
      - count how many nodes you pop/expand
    """
    nodes_expanded=0
    frontier=[]
    heapq.heappush(frontier,(heuristic(start, goal,connectivity),0,start))
    came_from={start: None}
    cost_so_far={start:0}
    while frontier:
      f_cost,current_cost, current=heapq.heappop(frontier)
      if current_cost>cost_so_far[current]:

        continue
      nodes_expanded+=1

      if current==goal:
        return reconstruct_path(came_from, goal),nodes_expanded
      for next_cell in neighbors(grid, current, connectivity):
        new_cost=cost_so_far[current]+cost(grid, current, next_cell)
        new_f=new_cost+heuristic(next_cell,goal,connectivity)
        if next_cell not in cost_so_far or new_cost< cost_so_far[next_cell]:
          cost_so_far[next_cell]=new_cost
          came_from[next_cell]=current
          heapq.heappush(frontier,(new_f,new_cost,next_cell))
          
    
    return None, nodes_expanded