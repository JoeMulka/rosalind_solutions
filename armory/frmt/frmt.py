# https://rosalind.info/problems/frmt/
from Bio import Entrez
from Bio import SeqIO
from sys import stdout

Entrez.email = "joseph.mulka1@gmail.com"

id_list = [
    "JQ867090",
    "JQ712981",
    "NM_204821",
    "JX308821",
    "JX205496",
    "JQ011270",
    "JX914595",
    "NM_001131214",
]

handle = Entrez.efetch(db="nucleotide", id=id_list, rettype="fasta")

records = list(SeqIO.parse(handle, "fasta"))
shortest_record_length = -1
shortest_record = None
for record in records:
    if len(record.seq) < shortest_record_length or shortest_record_length == -1:
        shortest_record_length = len(record.seq)
        shortest_record = record
SeqIO.write(shortest_record, stdout, "fasta")
