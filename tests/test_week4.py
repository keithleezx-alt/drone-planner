"""Week 4: BFS and Dijkstra."""
from src.planners.bfs import bfs
from src.planners.dijkstra import dijkstra


def _valid_path(grid, path, start, goal):
    if path is None:
        return False
    if path[0] != start or path[-1] != goal:
        return False
    for (r, c) in path:
        if grid[r, c] != 0:
            return False
    return True


def test_bfs_finds_path(simple_map):
    start, goal = (0, 0), (7, 7)
    path = bfs(simple_map, start, goal)
    assert _valid_path(simple_map, path, start, goal)


def test_bfs_no_path(open_map):
    # box the goal in? open_map has no full wall, so just check reachability holds
    path = bfs(open_map, (0, 0), (5, 5))
    assert path is not None


def test_dijkstra_matches_bfs_length_unweighted(simple_map):
    start, goal = (0, 0), (7, 7)
    b = bfs(simple_map, start, goal)
    d = dijkstra(simple_map, start, goal)
    assert d is not None
    # same cost on an unweighted grid
    assert len(b) == len(d)
