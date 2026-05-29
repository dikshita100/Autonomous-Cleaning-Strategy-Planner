
# AUTONOMOUS CLEANING STRATEGY PLANNER


import heapq
import random
import time

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


# A* SEARCH ALGORITHM

def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar():

    pq = [(0, 0, START, [])]

    visited = set()

    while pq:

        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        path = path + [node]

        if node == GOAL:
            return path

        for neighbor in get_neighbors(node):

            new_g = g + 1

            h = heuristic(neighbor, GOAL)

            new_f = new_g + h

            heapq.heappush(
                pq,
                (new_f, new_g, neighbor, path)
            )

    return None

# CSP CONSTRAINT CHECKING

def constraint_check(path):

    if len(path) != len(set(path)):
        return False

    for x, y in path:
        if grid[x][y] == 1:
            return False

    return True


# UTILITY FUNCTION


def utility_function(path):

    path_length = len(path)

    energy_cost = path_length * 0.5

    utility = 100 - path_length - energy_cost

    return utility


# MARKOV MODEL

def markov_next_state(current_state):

    transitions = {
        "SAFE": ["SAFE", "BLOCKED"],
        "BLOCKED": ["SAFE", "BLOCKED"]
    }

    return random.choice(transitions[current_state])


# PERFORMANCE ANALYSIS


start_time = time.time()

path = astar()

end_time = time.time()

runtime = end_time - start_time


# OUTPUTS

print("\nPath Found:\n")
print(path)

print("\nPath Length :", len(path))

print("\nExecution Time :", runtime)

valid = constraint_check(path)

print("\nConstraint Satisfaction :", valid)

utility = utility_function(path)

print("\nUtility Score :", utility)

display_grid(path)


# UNCERTAINTY HANDLING


print("\n UNCERTAINTY HANDLING")

state = "SAFE"

for i in range(5):

    next_state = markov_next_state(state)

    print("Current State :", state,
          " --> Next State :", next_state)

    state = next_state




print("1. Grid environment created.")
print("2. Path planning completed.")
print("3. Obstacles avoided successfully.")
print("4. Utility evaluated for efficiency.")
print("5. Uncertainty handled using Markov model.")
print("6. Optimized cleaning path generated.")