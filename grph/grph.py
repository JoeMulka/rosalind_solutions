from Bio import SeqIO

data_path = "rosalind_grph.txt"
k_val = 3


#pref_suff_library = {}
prefix_library = {}
suffix_library = {}
with open(data_path, "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        prefix = str(record.seq[:k_val])
        suffix = str(record.seq[-k_val:])
        #pref_suff_library[record.id] = (prefix, suffix)
        if prefix in prefix_library:
            prefix_library[prefix].append(record.id)
        else:
            prefix_library[prefix] = [record.id]
        if suffix in suffix_library:
            suffix_library[suffix].append(record.id)
        else:
            suffix_library[suffix] = [record.id]

graph = {}
for prefix in prefix_library:
    if prefix in suffix_library:
        # There is a prefix/suffix match
        # There could be multiple ids in each list
        for id1 in prefix_library[prefix]:
            for id2 in suffix_library[prefix]:
                if id1 != id2:
                    # prevent loops on the same id/node
                    if id1 in graph:
                        graph[id1].append(id2)
                    else:
                        graph[id1] = [id2]
# Take a look at the graph in dictionary form
print(graph)
# Generate an edge list
with open("grph_out.txt", "w") as out_handle:
    for source_node in graph:
        for dest_node in graph[source_node]:
            out_handle.write(f"{dest_node} {source_node}\n")
