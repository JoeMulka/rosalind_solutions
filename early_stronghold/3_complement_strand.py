import os

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "3_rosalind_revc.txt")

# Check if data path file exists
if os.path.exists(data_path):
    with open(data_path, "r") as infile:
        input_data = infile.readlines()

else:
    sample = "AAAACCCGGT"
    input_data = [sample]


def complement_base(base):
    base = base.upper()
    match base:
        case "A":
            return "T"
        case "T":
            return "A"
        case "C":
            return "G"
        case "G":
            return "C"


all_output = []
for line in input_data:
    # output is the reverse complement of the input
    output_line = ""
    for base in reversed(line):
        output_line += complement_base(base)

    all_output.append(output_line)
print(all_output)
