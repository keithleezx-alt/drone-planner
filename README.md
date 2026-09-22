# Drone Planner Sprint — Intern Workspace

jingyi has been here :)-person b
Welcome. Over 7 weeks you'll build a 2D path planner from scratch — command line
and git first, then BFS, Dijkstra, A\*, and RRT. This repo is **your workspace**:
it ships with folders, stub files, and tests. Your job is to fill in the stubs
until the tests pass, one week at a time.

There is a separate **reference repo** (your mentor has the link). Try each week
yourself *before* looking at it.

---

## How this works — read this once, fully

Every week follows the same loop. This loop *is* the point — by week 3 it should
be automatic.

1. **Start the week on a fresh branch**
   ```bash
   git checkout main
   git pull
   git checkout -b week-3-grid
   ```
2. **Do the week's tasks** (see `docs/week-XX.md`). Commit as you go — small,
   meaningful commits, not one giant commit at the end.
   ```bash
   git add src/grid/grid.py
   git commit -m "Add 8-connected neighbor lookup"
   ```
3. **Run the tests for that week** until they pass:
   ```bash
   pytest tests/test_week3.py -v
   ```
4. **Push and open a Pull Request** into `main`. Fill in the PR checklist.
   ```bash
   git push -u origin week-3-grid
   ```
   Then open the PR on GitHub.
5. **Your mentor reviews the PR.** Address comments by pushing more commits to the
   same branch. When approved, **you merge it**.
6. Next week, branch off the updated `main` again.

> The PR is the deliverable each week. "It works on my machine" doesn't count
> until it's a merged PR with green tests.

---

## One-time setup (Week 1)

```bash
# clone your copy
git clone <your-repo-url>
cd drone-planner-sprint

# make a virtual environment and activate it
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# confirm everything runs
pytest -v
```

At the start you'll see most tests **fail** — that's expected. They turn green as
you implement each week.

---

## Repo layout

```
src/
  grid/        grid map representation + helpers  (Week 3)
  planners/    bfs, dijkstra, astar, rrt          (Weeks 4-6)
tests/         one test file per week — your target
maps/          sample maps to plan across
benchmarks/    compare planners (Week 7)
docs/          the week-by-week task briefs
```

## The 7 weeks at a glance

| Week | Branch name          | You deliver                                  |
|------|----------------------|----------------------------------------------|
| 1    | `week-1-setup`       | venv + a hello-world script, run from CLI    |
| 2    | `week-2-git`         | this repo cloned, a practice PR merged       |
| 3    | `week-3-grid`        | grid map + neighbor lookup + visualization   |
| 4    | `week-4-bfs-dijkstra`| working BFS and Dijkstra                     |
| 5    | `week-5-astar`       | working A\* + comparison write-up            |
| 6    | `week-6-rrt`         | RRT (and RRT\* if time)                       |
| 7    | `week-7-benchmark`   | benchmark script + README + short reflection |

Full task briefs and resources are in `docs/`.

## Ground rules

- Ask early. Stuck for 30+ minutes with no progress → ask your mentor.
- Commit messages describe *what changed and why*, not "fix" or "update".
- Never commit your `.venv/` (it's in `.gitignore` already).
- Understand before you copy. If you use the reference repo, retype and explain it.

> Run the benchmark as a module: `python -m benchmarks.compare`
