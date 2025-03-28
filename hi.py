import graphviz

# Create a directed graph
fsa = graphviz.Digraph(format="png")

# Define states
states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"]
final_states = ["q1", "q2", "q4", "q5", "q6", "q9"]  # Accepting states

# Add nodes
for state in states:
    if state in final_states:
        fsa.node(state, shape="doublecircle")  # Final states
    else:
        fsa.node(state, shape="circle")  # Normal states

# Add transitions
fsa.edge("q0", "q1", label="BAKE")  # Base word transition

# Variations of "BAKE"
fsa.edge("q1", "q2", label="D")  # BAKED
fsa.edge("q1", "q3", label="R")  # BAKER, BAKERY
fsa.edge("q3", "q4", label="Y")  # BAKERY
fsa.edge("q3", "q5", label="S")  # BAKERS
fsa.edge("q1", "q6", label="S")  # BAKES
fsa.edge("q1", "q7", label="I")  # BAKING part 1
fsa.edge("q7", "q8", label="N")  # BAKING part 2
fsa.edge("q8", "q9", label="G")  # BAKING part 3

# Render and save
fsa_path = "/mnt/data/fsa_bake.png"
fsa.render(filename=fsa_path, format="png", cleanup=True)
fsa_path
