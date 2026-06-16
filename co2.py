# -------------------- CO2 --------------------
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
