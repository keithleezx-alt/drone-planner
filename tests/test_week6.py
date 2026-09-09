"""Week 6: RRT (continuous 2D over the grid)."""
import math
from src.planners.rrt import rrt


def test_rrt_returns_path_open(open_map):
    # open map, plan from one free corner to another
    path = rrt(open_map, (0.0, 0.0), (5.0, 5.0), step=1.0, max_iters=20000)
    assert path is not None
    assert math.dist(path[0], (0.0, 0.0)) < 1e-6
    # ends near goal
    assert math.dist(path[-1], (5.0, 5.0)) <= 1.5
