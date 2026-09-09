"""Grid map representation for 2D path planning.

Convention used everywhere in this repo:
  - a map is a 2D numpy array
  - 0 means FREE, 1 means OBSTACLE
  - a cell is a (row, col) tuple
  - (0, 0) is top-left

You are GIVEN load_map() and show_grid() so you can focus on the algorithms.
You must IMPLEMENT neighbors() in Week 3.
"""

from __future__ import annotations

import numpy as np

FREE = 0
OBSTACLE = 1


def load_map(path: str) -> np.ndarray:
    """Load a map from a plain-text file of 0s and 1s (space or no space).

    Example file:
        0 0 0 1 0
        0 1 0 1 0
        0 1 0 0 0
    Returns a 2D numpy array of ints.
    """
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cells = line.replace(" ", "")
            rows.append([int(c) for c in cells])
    return np.array(rows, dtype=int)


def in_bounds(grid: np.ndarray, cell: tuple[int, int]) -> bool:
    r, c = cell
    return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]


def is_free(grid: np.ndarray, cell: tuple[int, int]) -> bool:
    return in_bounds(grid, cell) and grid[cell] == FREE


def neighbors(
    grid: np.ndarray, cell: tuple[int, int], connectivity: int = 4
) -> list[tuple[int, int]]:
    """Return valid neighbor cells of `cell`.

    TODO (Week 3):
      - connectivity == 4: up, down, left, right
      - connectivity == 8: also the four diagonals
      - only return cells that are in bounds AND free
    Hint: build the list of candidate offsets, add them to (r, c),
    then filter with is_free().
    """
    raise NotImplementedError("Week 3: implement neighbors()")


def show_grid(grid: np.ndarray, path=None, start=None, goal=None, title="grid"):
    """Visualize a grid, and optionally a path and start/goal.

    Given to you — no need to modify. Requires matplotlib.
    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.imshow(grid, cmap="Greys", origin="upper")
    if path:
        ys = [c for r, c in path]
        xs = [r for r, c in path]
        ax.plot(ys, xs, linewidth=2)
    if start:
        ax.scatter([start[1]], [start[0]], marker="o", s=80)
    if goal:
        ax.scatter([goal[1]], [goal[0]], marker="*", s=120)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
