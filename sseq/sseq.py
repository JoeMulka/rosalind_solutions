from Bio import SeqIO

fasta_path = "rosalind_sseq.fasta"


with open(fasta_path, "r") as handle:
    records = list(SeqIO.parse(handle, "fasta"))
parent_sequence = records[0].seq
target_subseq = records[1].seq

# Can pop symbols from the subseq as we find them while traversing the parent seq from left to right
subseq_indices = []
for index, char in enumerate(parent_sequence):
    if target_subseq[0] == char:
        subseq_indices.append(str(index + 1))
        target_subseq = target_subseq[1:]
    if len(target_subseq) == 0:
        break
print(" ".join(subseq_indices))
