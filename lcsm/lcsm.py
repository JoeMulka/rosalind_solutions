from Bio import motifs, SeqIO
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
import re
import subprocess

test_input_path = "rosalind_lcsm.txt"
aligned_path = "clustal_output.fasta"
min_motif_length = 2

# First, align the sequences to each other
output = subprocess.check_output(["clustalo","-i",test_input_path,"-o",aligned_path])

sequences = []
with open(aligned_path,"r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        sequences.append(record.seq)

# The motif finder in biopython won't work without alignment because it requires all input k-mers to be the same length
motif = motifs.create(sequences,alphabet="-ACGT")

sequence_length = len(sequences[0])
consensus_bases = ["N"] * sequence_length
num_sequences = len(sequences)
for base in "ACGT":
    for i,base_count in enumerate(motif.counts[base]):
        if base_count == num_sequences:
            consensus_bases[i] = base

consensus_string = "".join(consensus_bases)
#consensus_string = "NNATATATNNNNNGTACGTNNNNNNNGTNNN"

candidate_motifs = re.findall(r"[ACTG]+",consensus_string)

print(max(candidate_motifs,key=len))
