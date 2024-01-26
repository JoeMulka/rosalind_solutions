import networkx as nx
import matplotlib.pyplot as plt
import scipy

input_path = "rosalind_tree.txt"
with open(input_path, "r") as f:
    num_nodes = int(f.readline().strip())
    initial_edges = f.readlines()
    initial_edges = [edge.strip().split() for edge in initial_edges]
    initial_edges = [(int(edge[0]), int(edge[1])) for edge in initial_edges]

G = nx.Graph()
G.add_nodes_from(range(1, num_nodes + 1))
G.add_edges_from(initial_edges)

# Find the existing subtrees in the graph
subtrees = nx.connected_components(G)

# Add new edges connecting the subtrees
# Start by grabbing a node from any subtree, the first works fine
new_root = next(subtrees).pop()
num_new_edges = 0

# Casting to list so we can get the number of edges before the loop
# For the purpose of the Rosalind problem, we really only need the number of new edges,
# so break after printing the length of this list on large graphs
subtrees = list(subtrees)
print(f"Subtrees: {len(subtrees)}")
for subtree in subtrees:
    num_new_edges += 1
    # Connect the new root to the first node in the subtree
    G.add_edge(new_root, subtree.pop())

print(f"Number of new edges: {num_new_edges}")
# visualize
nx.draw_networkx(G)
plt.show()
