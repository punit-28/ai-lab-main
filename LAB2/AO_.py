# -------------------------------
# AO* Algorithm
# -------------------------------

# Graph:
# A has two OR choices:
# A -> B
# A -> C
#
# B is an AND node:
# B -> D AND E

graph = {
    'A': [
        [('B', 1)],
        [('C', 4)]
    ],

    'B': [
        [('D', 2), ('E', 3)]
    ],

    'C': [
        [('F', 2)]
    ],

    'D': [],
    'E': [],
    'F': []
}

# -------------------------------
# Heuristic Values
# -------------------------------
heuristic = {
    'A': 6,
    'B': 3,
    'C': 4,
    'D': 0,
    'E': 0,
    'F': 0
}


# -------------------------------
# AO* Function
# -------------------------------
def ao_star(node):

    # If node is a goal/leaf
    if not graph[node]:
        return heuristic[node], [node]

    best_cost = float('inf')
    best_solution = None

    # Each group represents an OR choice
    for option in graph[node]:

        total_cost = 0
        solution = [node]

        # All nodes inside an option are AND
        for child, cost in option:

            child_cost, child_solution = ao_star(child)

            total_cost += cost + child_cost
            solution += child_solution

        # Choose minimum-cost OR option
        if total_cost < best_cost:
            best_cost = total_cost
            best_solution = solution

    return best_cost, best_solution


# -------------------------------
# Start Node
# -------------------------------
start = 'A'

# -------------------------------
# Run AO*
# -------------------------------
cost, solution = ao_star(start)

# -------------------------------
# Output
# -------------------------------
print("AO* Algorithm")
print("Solution:", solution)
print("Cost:", cost)