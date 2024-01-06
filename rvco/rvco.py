from Bio import SeqIO

data_path = "rosalind_rvco.txt"

revcomp_matches = 0
with open(data_path, "r") as input_handle:
     for record in SeqIO.parse(input_handle,"fasta"):
          if record.seq == record.reverse_complement().seq:
               revcomp_matches += 1

print(f"Found {revcomp_matches} matching reverse complements in {data_path}")