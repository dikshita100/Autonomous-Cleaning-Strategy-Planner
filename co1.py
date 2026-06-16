import heapq
import random
import time

# -------------------- CO1 --------------------
# PEAS MODEL

print("\n PEAS MODEL")

print("Performance  : Maximum cleaning coverage")
print("Environment  : Indoor cleaning grid")
print("Actuators    : Robot movement")
print("Sensors      : Obstacle detector")


# GRID ENVIRONMENT

grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

ROWS = len(grid)
COLS = len(grid[0])

START = (0, 0)
GOAL = (4, 4)

# DISPLAY GRID

def display_grid(path=None):

    temp = [row[:] for row in grid]

    if path:
        for x, y in path:
            if (x, y) != START and (x, y) != GOAL:
                temp[x][y] = "*"

    temp[START[0]][START[1]] = "S"
    temp[GOAL[0]][GOAL[1]] = "G"

    print("\nGrid Environment:\n")

    for row in temp:
        print(row)


# VALID MOVE

def is_valid(x, y):

    return (
        0 <= x < ROWS and
        0 <= y < COLS and
        grid[x][y] != 1
    )

# NEIGHBOR FUNCTION

def get_neighbors(node):

    x, y = node

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        if is_valid(nx, ny):
            neighbors.append((nx, ny))

    return neighbors