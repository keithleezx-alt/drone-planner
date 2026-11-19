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
from src.planners.bfs import reconstruct_path
from src.grid.grid import is_free

def euclidean_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def check_collision_free(grid, start, end):
    deltaX, deltaY = end[0] - start[0], end[1] - start[1]
    progress = 0.05
    while progress < 1:
        pointX, pointY = start[0] + deltaX * progress, start[1] + deltaY * progress
        if not is_free(grid, (round(pointX), round(pointY))):
            return 0
        progress += 0.05
    return 1

def path_length(path):
    distance = 0
    for i in range(len(path)-1):
        distance += euclidean_distance(path[i], path[i+1])
    return distance

def tree_distance(came_from, goal):
    path = reconstruct_path(came_from, goal)
    return path_length(path)

def rrt(grid, start, goal, step=1.0, max_iters=5000, goal_bias=0.05):
    """Grow an RRT from start toward goal in continuous 2D.

    Return a list of (x, y) points from start to goal, or None.
    """
    came_from = dict()
    came_from[start] = None
    nodes = [start]
    if euclidean_distance(start, goal) <= step and check_collision_free(grid, start, goal):
        return [start, goal]

    for iteration in range(max_iters):
        # sample a random point
        samplePoint = None
        if random.random() < goal_bias:
            samplePoint = goal
        else:
            sizeX, sizeY = grid.shape
            sampleX = sizeX * random.random()
            sampleY = sizeY * random.random()
            samplePoint = (sampleX, sampleY)

        # find nearest node
        nearest_distance = math.inf
        nearest_point = None
        for point in nodes:
            distance = euclidean_distance(point, samplePoint)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_point = point
        if nearest_distance < 1e-10:
            continue

        # steer by step
        deltaX = samplePoint[0] - nearest_point[0]
        deltaY = samplePoint[1] - nearest_point[1]
        deltaX = deltaX / nearest_distance * step
        deltaY = deltaY / nearest_distance * step
        steered_point = (nearest_point[0] + deltaX, nearest_point[1] + deltaY)

        # check if collision free
        # check all cells within bounding box, to see if they lie on path
        if not check_collision_free(grid, nearest_point, steered_point):
            continue

        came_from[steered_point] = nearest_point
        nodes.append(steered_point)

        if euclidean_distance(steered_point, goal) <= step and check_collision_free(grid, steered_point, goal):
            came_from[goal] = steered_point
            return reconstruct_path(came_from, goal)

def rrt_star(grid, start, goal, goal_bias=0.05, step=1.0, max_iters=5000, radius=2.0):
    """RRT* — like RRT but rewire nearby nodes to lower-cost parents.
    """
    came_from = dict()
    came_from[start] = None
    nodes = [start]
    if euclidean_distance(start, goal) <= step and check_collision_free(grid, start, goal):
        return [start, goal]

    for iteration in range(max_iters):
        # sample a random point
        samplePoint = None
        if random.random() < goal_bias:
            samplePoint = goal
        else:
            sizeX, sizeY = grid.shape
            sampleX = sizeX * random.random()
            sampleY = sizeY * random.random()
            samplePoint = (sampleX, sampleY)

        # find best node
        nearest_distance = math.inf
        nearest_point = None
        for point in nodes:
            distance = euclidean_distance(point, samplePoint)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_point = point
        if nearest_distance < 1e-10:
            continue

        # steer by step
        deltaX = samplePoint[0] - nearest_point[0]
        deltaY = samplePoint[1] - nearest_point[1]
        deltaX = deltaX / nearest_distance * step
        deltaY = deltaY / nearest_distance * step
        steered_point = (nearest_point[0] + deltaX, nearest_point[1] + deltaY)

        best_distance = math.inf
        best_parent = None
        for point in nodes:
            distance = euclidean_distance(point, steered_point)
            if distance > radius:
                continue
            if not check_collision_free(grid, point, steered_point):
                continue
            distance += tree_distance(came_from, point)
            if distance < best_distance:
                best_distance = distance
                best_parent = point

        if best_parent is None:
            continue

        came_from[steered_point] = best_parent
        nodes.append(steered_point)

        for point in nodes:
            distance = euclidean_distance(point, steered_point)
            if distance > radius:
                continue
            if not check_collision_free(grid, point, steered_point):
                continue
            distance += tree_distance(came_from, steered_point)
            if distance < tree_distance(came_from, point):
                came_from[point] = steered_point

    best_distance = math.inf
    best_parent = None
    for end_point in nodes:
        distance = euclidean_distance(end_point, goal)
        if distance > radius:
            continue
        if not check_collision_free(grid, end_point, goal):
            continue
        distance += tree_distance(came_from, end_point)
        if distance < best_distance:
            best_distance = distance
            best_parent = end_point
    if best_parent is None:
        return None
    came_from[goal] = best_parent
    return reconstruct_path(came_from, goal)

def show_grid(grid: np.ndarray, path1=None, path2=None, start=None, goal=None, title="grid"):
    """Visualize a grid, and optionally a path and start/goal.
    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.imshow(grid, cmap="Greys", origin="upper")
    if path1:
        ys = [c for r, c in path1]
        xs = [r for r, c in path1]
        ax.plot(ys, xs, linewidth=2, color='red')
    if path2:
        ys = [c for r, c in path2]
        xs = [r for r, c in path2]
        ax.plot(ys, xs, linewidth=2, color='green')
    if start:
        ax.scatter([start[1]], [start[0]], marker="o", s=80)
    if goal:
        ax.scatter([goal[1]], [goal[0]], marker="*", s=120)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

def compare_algorithms(grid):
    h, w = grid.shape
    path_rrt = rrt(grid, (0.0, 0.0), (h-1, w-1), step=1.0, max_iters=20000)
    path_rrt_star = rrt_star(grid, (0.0, 0.0), (h-1, w-1), step=1.0, max_iters=200)
    show_grid(grid, path1=path_rrt, path2=path_rrt_star, start=(0.0,0.0), goal=(h-1, w-1))

def load_map(path: str) -> np.ndarray:
    """Load a map from a plain-text file of 0s and 1s (space or no space).

    Example file:
        0 0 0 1 0
        0 1 0 1 0
        0 1 0 0 0
    Returns a 2D numpy array of ints.
    """
    import numpy as np
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cells = line.replace(" ", "")
            rows.append([int(c) for c in cells])
    return np.array(rows, dtype=int)

def main():
    grid = load_map("maps/simple.txt")
    compare_algorithms(grid)

if __name__ == "__main__":
    main()
