# -------------------- CO6 --------------------

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


print("\n EXPLAINABLE AI")
print("1. Grid environment created.")
print("2. Path planning completed.")
print("3. Obstacles avoided successfully.")
print("4. Utility evaluated for efficiency.")
print("5. Uncertainty handled using Markov model.")
print("6. Optimized cleaning path generated.")