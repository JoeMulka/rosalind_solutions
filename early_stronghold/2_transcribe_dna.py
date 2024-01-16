sample = "GATGGAACTTGACTACGTAAATT"
data_path = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data\rosalind_rna.txt"

with open(data_path, "r") as infile:
    input_data = infile.read()

transcribed = "".join([x if x != "T" else "U" for x in input_data])

print(transcribed)
