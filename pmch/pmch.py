from itertools import combinations, chain
import networkx as nx
import matplotlib.pyplot as plt
from math import comb


#sequence = "AGCUAGUCAU"
sequence = "ACGAUCGUGACACGCUGGCUUCGGACCGUCGACUUACAGCCGUACUACGCAAUUGACUGGUAGCUACGUAGGAUGC"
match_dict = {"A":"U","U":"A","C":"G","G":"C"}
edges = []

for i,source_base in enumerate(sequence):
    for j,dest_base in enumerate(sequence):
        # Check if the bases are complementary
        if match_dict[source_base] == dest_base:
            # Check if the match is already in the edges list in reverse
            if not (j,i) in edges:
                # Add the edge to the list
                edges.append((i,j))


#G = nx.Graph()
#G.add_edges_from(edges)

# Visualize the graph
#nx.draw(G, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray', node_size=800)

# Show the plot
#plt.show()

# Now we look for subsets of the edges that satisfy the perfect condition
# That is, sets that include ever node, but no node is found in two edges
# There should be exactly len(sequence) / 2 edges in any such set
selection_size = len(sequence) // 2
candidate_sets = combinations(edges,selection_size)
perfect_match_sets = 0
num_processed = 0
print("number of candidates: " + str(comb(len(edges),selection_size)))
print("evaluating candidates")
for candidate in candidate_sets:
    flattened = set(chain(*candidate))
    num_processed += 1
    if num_processed % 100000 == 0:
        #print(num_processed)
        pass
    if len(flattened) == len(sequence):
        perfect_match_sets +=1
        if False:
            num_print += 1
            print(candidate)
            for edge in candidate:
                print(f"{sequence[edge[0]]} {sequence[edge[1]]}")
print(perfect_match_sets)