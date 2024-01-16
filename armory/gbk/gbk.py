from Bio import Entrez

Entrez.email = "joseph.mulka1@gmail.com"

handle = Entrez.esearch(
    db="nucleotide",
    term='"Prevotella"[Organism] AND ("2001/07/10"[PDAT] : "2005/11/11"[PDAT])',
)

record = Entrez.read(handle)
print(record)
