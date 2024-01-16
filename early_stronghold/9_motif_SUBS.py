import os

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "9_rosalind_subs.txt")

# Check if data path file exists
if os.path.exists(data_path):
    with open(data_path, "r") as infile:
        seq1, seq2 = infile.readlines()
        seq1 = seq1.strip()
        seq2 = seq2.strip()
else:
    seq1 = "GATATATGCATATACTT"
    seq2 = "ATAT"

print(seq1, seq2)

location_list = []
for index in range(0, len(seq1)):
    if seq1[index : index + len(seq2)] == seq2:
        location_list.append(index + 1)

print(*location_list)
