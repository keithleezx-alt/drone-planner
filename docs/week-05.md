# Week 5 — A* Algorithm

**Milestone:** Working A* that expands fewer nodes than Dijkstra on the same map,
with a short write-up of why.

## Branch
`week-5-astar`

## Tasks
- [ ] Implement `heuristic()` (Manhattan for 4-conn, octile/Euclidean for 8).
- [ ] Implement `astar()`, returning `(path, nodes_expanded)`.
- [ ] Compare nodes expanded vs. Dijkstra; write findings in `docs/astar-notes.md`.
- [ ] Make `pytest tests/test_week5.py -v` pass.

## Concurrent paper
LaValle (1998), *Rapidly-Exploring Random Trees: A New Tool for Path Planning*
(read ahead of Week 6).

## Resources
- Red Blob Games implementation: https://www.redblobgames.com/pathfinding/a-star/implementation.html
- Amit's heuristics guide: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
