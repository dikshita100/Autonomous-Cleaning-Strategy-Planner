# -------------------- CO4 --------------------

# UTILITY FUNCTION

def utility_function(path):

    path_length = len(path)

    energy_cost = path_length * 0.5

    utility = 100 - path_length - energy_cost

    return utility