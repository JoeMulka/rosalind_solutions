import os

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "6_rosalind_hamm.txt")

# Check if data path file exists
if os.path.exists(data_path):
    with open(data_path, "r") as infile:
        lines = infile.readlines()
        input_1 = lines[0]
        input_2 = lines[1]
else:
    input_1 = "GAGCCTACTAACGGGAT"
    input_2 = "CATCGTAATGACGGCCT"

ham_dist = 0
for base1, base2 in zip(input_1, input_2):
    if base1.upper() != base2.upper():
        ham_dist += 1

print(ham_dist)
