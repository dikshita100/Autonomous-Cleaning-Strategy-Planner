# -------------------- CO3 --------------------
# CSP CONSTRAINT CHECKING

def constraint_check(path):

    if len(path) != len(set(path)):
        return False

    for x, y in path:
        if grid[x][y] == 1:
            return False

    return True