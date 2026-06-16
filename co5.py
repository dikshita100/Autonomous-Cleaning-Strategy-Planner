# -------------------- CO5 --------------------
# MARKOV MODEL

def markov_next_state(current_state):

    transitions = {
        "SAFE": ["SAFE", "BLOCKED"],
        "BLOCKED": ["SAFE", "BLOCKED"]
    }

    return random.choice(transitions[current_state])