from collections import Counter

sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
data_path = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data\rosalind_dna.txt"
with open(data_path, "r") as infile:
    input_string = infile.read()

counted = Counter(input_string)

print("{} {} {} {}".format(counted["A"], counted["C"], counted["G"], counted["T"]))
