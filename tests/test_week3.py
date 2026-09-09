"""Week 3: grid representation + neighbors."""
import numpy as np
from src.grid.grid import load_map, is_free, neighbors, in_bounds


def test_map_loads(simple_map):
    assert simple_map.shape == (8, 8)
    assert simple_map[0, 0] == 0


def test_in_bounds(simple_map):
    assert in_bounds(simple_map, (0, 0))
    assert not in_bounds(simple_map, (-1, 0))
    assert not in_bounds(simple_map, (8, 8))


def test_neighbors_4_connected_center(open_map):
    # (0,0) corner on open map has 2 free 4-neighbors
    n = neighbors(open_map, (0, 0), connectivity=4)
    assert set(n) == {(0, 1), (1, 0)}


def test_neighbors_excludes_obstacles(open_map):
    # cell (1,1) sits next to the 2x2 obstacle block at rows2-3,cols2-3
    n = neighbors(open_map, (1, 2), connectivity=4)
    assert (2, 2) not in n  # that's an obstacle


def test_neighbors_8_connected_count(open_map):
    n = neighbors(open_map, (0, 0), connectivity=8)
    assert set(n) == {(0, 1), (1, 0), (1, 1)}
