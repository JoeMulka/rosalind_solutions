from Bio import SeqIO

data_path = "rosalind_splc.txt"

with open(data_path,"r") as infile:
    records = SeqIO.parse(infile,"fasta")
    mrna_sequence = next(records).seq
    introns = [record.seq for record in list(records)]

for intron in introns:
    mrna_sequence = mrna_sequence.replace(intron,"")
print(mrna_sequence.translate())