"""Rapidly-exploring Random Tree (Week 6).

Grid search doesn't scale to high dimensions or continuous space. RRT instead
grows a tree by randomly sampling points and steering toward them, quickly
covering free space. RRT* adds rewiring so the path quality improves over time.

Here we work in continuous 2D: a point is (x, y) as floats, and obstacles are
checked against the same 0/1 grid (a point is in collision if its cell is 1).
"""

from __future__ import annotations

import math
import random


def rrt(grid, start, goal, step=1.0, max_iters=5000, goal_bias=0.05):
    """Grow an RRT from start toward goal in continuous 2D.

    Return a list of (x, y) points from start to goal, or None.

    TODO (Week 6):
      - sample a random point (with goal_bias chance, sample the goal)
      - find the nearest node in the tree
      - steer from it toward the sample by `step`
      - if the new point and edge are collision-free, add it to the tree
      - stop when you get within `step` of the goal
    Hint: keep nodes as a list and a parent dict for path reconstruction.
    """
    raise NotImplementedError("Week 6: implement rrt()")


def rrt_star(grid, start, goal, step=1.0, max_iters=5000, radius=2.0):
    """RRT* — like RRT but rewire nearby nodes to lower-cost parents.

    TODO (Week 6, stretch): implement after rrt() works.
    """
    raise NotImplementedError("Week 6 (stretch): implement rrt_star()")
