from Bio.Data import CodonTable

sample_data = "MA"
input_data = sample_data
with open("rosalind_mrna.txt","r") as infile:
    input_data = infile.read().strip()

input_data = input_data +  "*"

arithmetic_modulo = 1000000

rna_forward_table = CodonTable.standard_rna_table.forward_table
rna_forward_table["UAA"] = "*"
rna_forward_table["UAG"] = "*"
rna_forward_table["UGA"] = "*"
# We need an rna back table, but the one from CodonTable does not contain the ambiguous codons
rna_back_table = {}
for triplet in rna_forward_table:
    amino = rna_forward_table[triplet]
    if amino in rna_back_table:
        rna_back_table[amino].append(triplet)
    else:
        rna_back_table[amino] = [triplet]

# For the purposes of this question, we are really only interested in the number of codons that correlate to each amino
codons_per_amino = {single_amino : len(rna_back_table[single_amino]) for single_amino in rna_back_table}
print(codons_per_amino)

total_possibilities = 1
for amino in input_data:
    base_possibilities = codons_per_amino[amino]
    total_possibilities = ((total_possibilities % arithmetic_modulo) * (base_possibilities % arithmetic_modulo)) % arithmetic_modulo


print(f"total possibilities: {total_possibilities}")