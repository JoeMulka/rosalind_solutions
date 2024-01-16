from Bio import Entrez
from Bio import SeqIO
import subprocess

with open("rosalind_need.txt", "r") as f:
    id_list = f.read().strip().split()

Entrez.email = "joseph.mulka1@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=id_list, rettype="fasta")

fasta_results = handle.read().strip().split("\n\n")
for id in id_list:
    with open(f"{id}.fasta", "w") as f:
        # agnostic of order but checks every entry for the id, not super fast
        for fasta_result in fasta_results:
            if id in fasta_result:
                f.write(fasta_result)

# Build bash needle command and then run with subprocess
needle_cmd = [
    "needle",
    "-asequence",
    f"{id_list[0]}.fasta",
    "-bsequence",
    f"{id_list[1]}.fasta",
    "-gapopen",
    "10",
    "-gapextend",
    "1",
    "-endopen",
    "10",
    "-endextend",
    "1",
    "-endweight",
    "-outfile",
    "needle.txt",
    "-brief",
]

output = subprocess.run(needle_cmd, capture_output=True, text=True)
print(output.stdout)
print(output.stderr)
