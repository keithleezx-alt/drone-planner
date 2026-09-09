# Week 6 — Sampling-Based Planning (RRT / RRT*)

**Milestone:** RRT finds a path through a continuous obstacle field; RRT* smooths
it.

## Branch
`week-6-rrt`

## Tasks
- [ ] Understand why grid search struggles in high dimensions.
- [ ] Implement `rrt()` in continuous 2D with goal bias.
- [ ] Make `pytest tests/test_week6.py -v` pass.
- [ ] (Stretch) implement `rrt_star()` and compare path quality.

## Concurrent paper
Karaman & Frazzoli (2011), *Sampling-based Algorithms for Optimal Motion
Planning* (RRT*). Skim the intuition; skip the proofs first pass.

## Resources
- CMU motion planning RRT lecture: https://www.cs.cmu.edu/~motionplanning/lecture/lec20.pdf
- LaValle's RRT page: http://lavalle.pl/rrt/
