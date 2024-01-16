# https://rosalind.info/problems/ini/


from Bio.Seq import Seq
import os

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "rosalind_ini.txt")

if os.path.exists(data_path):
    with open(data_path, "r") as infile:
        seq1 = str(infile.readlines())
        seq1 = seq1.strip()

else:
    seq1 = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"


my_seq = Seq(seq1)

for base in ["A", "C", "G", "T"]:
    print("{}".format(my_seq.count(base)), end=" ")
