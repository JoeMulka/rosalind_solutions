from Bio import SeqIO
import networkx as nx
import matplotlib.pyplot as plt


class Overlap:
    def __init__(self, left_seq, right_seq, left_index, right_index):
        self.left_seq = left_seq
        self.right_seq = right_seq
        self.left_index = left_index
        self.right_index = right_index

    def get_node(self):
        return (self.left_seq.id, self.right_seq.id)

    def get_indices(self):
        return (self.left_index, self.right_index)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (
            self.left_seq.id,
            self.right_seq.id,
        ) == (other.left_seq.id, other.right_seq).id

    def __hash__(self):
        return hash((self.left_seq.id, self.right_seq.id))

    def __str__(self):
        return f"Overlap between {self.left_seq.id} and {self.right_seq.id}"


# Compare two sequences to find out if the left seq overlaps the right seq
# Works by "aligning" the two sequences along their left edge and checking if they are equal
# Then "sliding" the left seq to the left and checking the new overlapping window for equality
def compare_seqs(left_seq, right_seq):
    num_shifts = 0
    while num_shifts <= min(len(left_seq) / 2, len(right_seq) / 2):
        # Start the left sequences part of the overlap at index num_shifts and continue to the end
        left_overlap = left_seq.seq[num_shifts:]
        # The right part of the overlap goes from the beginning and stops at the length of the left overlap
        right_overlap = right_seq.seq[: len(left_overlap)]
        if left_overlap == right_overlap:
            left_index = num_shifts
            right_index = len(left_seq) - num_shifts
            return (left_index, right_index)
        num_shifts += 1
    return None


# A function to find which sequences overlap with a given sequence
# Overlaps only count if they're more than half the length of both sequences
def find_overlaps(records):
    overlaps = []
    for seq_a in records:
        for seq_b in records:
            # We have found the target seq itself
            if seq_b.id == seq_a.id:
                continue
            # Neither string can be twice as long as the other without failing the condition of half length overlap
            if len(seq_b) < (len(seq_a) / 2):
                continue
            elif len(seq_a) < (len(seq_b) / 2):
                continue

            # First assume that target seq is the left seq in the overlap
            left_overlap = compare_seqs(seq_a, seq_b)
            # Then assume it is the right seq
            right_overlap = compare_seqs(seq_b, seq_a)

            if left_overlap:
                overlaps.append(Overlap(seq_a, seq_b, left_overlap[0], left_overlap[1]))
            if right_overlap:
                overlaps.append(
                    Overlap(seq_b, seq_a, right_overlap[0], right_overlap[1])
                )
    return overlaps


# Find the consensus sequence that the reads in the input came from
def find_consensus_sequence(overlaps, seq_dict):
    # Leftmost sequence should be the only one with outgoing edges but no incoming edges
    nodes = [overlap.get_node() for overlap in overlaps]
    graph = nx.DiGraph()
    graph.add_edges_from(nodes)
    no_in_edges = [node for node in graph.nodes if graph.in_degree(node) == 0]
    # Start with the longest of the nodes with no incoming edges
    start_read = no_in_edges[0]
    for edge in no_in_edges:
        if len(seq_dict[edge]) > len(seq_dict[start_read]):
            start_read = edge

    no_out_edges = [node for node in graph.nodes if graph.out_degree(node) == 0]

    # The ending edge is the longest edge with no outgoing edges
    # I'm not sure if this would be true "in the wild", but is true of this Rosalind problem
    for edge in no_out_edges:
        paths_to_target = nx.all_simple_paths(graph, source=start_read, target=edge)
        longest_path = max(paths_to_target, key=len)

    consensus_sequence = seq_dict[start_read]
    overlaps_hash_dict = {hash(obj): obj for obj in overlaps}
    # Start by adding the full sequence of the first node
    if print_alignment:
        print(seq_dict[start_read])
    offset = 0
    for left_node, right_node in zip(longest_path, longest_path[1:]):
        # Get the overlap object corresponding to this id
        this_overlap = overlaps_hash_dict[hash((left_node, right_node))]
        overhang = seq_dict[right_node][this_overlap.right_index :]
        consensus_sequence += overhang
        if print_alignment:
            print(
                (offset * " ") + (this_overlap.left_index * " ") + seq_dict[right_node]
            )
        offset += this_overlap.left_index
    return consensus_sequence


if __name__ == "__main__":
    input_fasta = "test_data.fasta"
    # input_fasta = "rosalind_long.txt"

    print_alignment = False

    with open(input_fasta, "r") as handle:
        records = list(SeqIO.parse(handle, "fasta"))

    seq_dict = {record.id: record.seq for record in records}

    overlaps = find_overlaps(records)
    consensus_sequence = find_consensus_sequence(overlaps, seq_dict)
    print(f"Consensus sequence: {consensus_sequence}")

    # Show a graph of the nodes
    nodes = [overlap.get_node() for overlap in overlaps]
    graph = nx.DiGraph()
    graph.add_edges_from(nodes)
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, arrows=True)
    plt.show()
