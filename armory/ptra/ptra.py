from Bio.Seq import translate

# Not every integer has a codon table associated with it, probably because some were removed after being added
# to the official list
table_ids = [
    1,
    2,
    3,
    4,
    5,
    6,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    33,
]

with open("rosalind_ptra.txt", "r") as f:
    lines = f.readlines()
    coding_dna = lines[0].strip()
    expected_protein_seq = lines[1].strip()
expected_protein_seq += "*"

# coding_dna = "ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
# expected_protein_seq = "MAMAPRTEINSTRING*"
successful_tables = []
for id in table_ids:
    attempted_translation = translate(coding_dna, table=id, to_stop=False)
    if attempted_translation == expected_protein_seq:
        successful_tables.append(id)
        # Break here if only interested in the first one
print(f"succesful translation tables: {successful_tables}")
