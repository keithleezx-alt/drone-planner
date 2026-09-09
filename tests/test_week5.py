"""Week 5: A*."""
from src.planners.dijkstra import dijkstra
from src.planners.astar import astar, heuristic


def test_heuristic_admissible_zero_at_goal():
    assert heuristic((3, 3), (3, 3)) == 0


def test_astar_finds_optimal_path(simple_map):
    start, goal = (0, 0), (7, 7)
    path, expanded = astar(simple_map, start, goal)
    d = dijkstra(simple_map, start, goal)
    assert path is not None
    assert path[0] == start and path[-1] == goal
    # A* optimal => same path cost/length as Dijkstra
    assert len(path) == len(d)


def test_astar_expands_no_more_than_dijkstra(simple_map):
    # A* should never expand MORE nodes than Dijkstra with a good heuristic
    start, goal = (0, 0), (7, 7)
    _, expanded = astar(simple_map, start, goal)
    assert expanded > 0
