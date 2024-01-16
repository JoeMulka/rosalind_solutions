import os

# import counter package
from collections import Counter

from gc_content_GC import ingest_fasta, FastARecord

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "10_rosalind_cons.txt")

# Check if data path file exists
if os.path.exists(data_path):
    fasta_records = ingest_fasta(data_path)
else:
    fasta_records = ingest_fasta(os.path.join(data_dir, "cons_sample.txt"))

column_sums = {base: [] for base in "ACGT"}
first_sequence = True
for record in fasta_records:
    for index, base in enumerate(record.sequence):
        if first_sequence:
            column_sums[base].append(1)
            other_bases = list(set("ACGT").difference(base))
            for other_base in other_bases:
                column_sums[other_base].append(0)
        else:
            column_sums[base][index] += 1
    first_sequence = False

consensus_sequence = ""
for index in range(0, len(column_sums["A"])):
    single_column = {
        "A": column_sums["A"][index],
        "T": column_sums["T"][index],
        "C": column_sums["C"][index],
        "G": column_sums["G"][index],
    }
    consensus_sequence += max(single_column, key=single_column.get)
print(consensus_sequence)
print("A:", *column_sums["A"])
print("C:", *column_sums["C"])
print("G:", *column_sums["G"])
print("T:", *column_sums["T"])
