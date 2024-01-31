mass_table_path = "mass_table.txt"
# test_protein = "SKADYEK"

rosalind_data_path = "rosalind_prtm.txt"
with open(rosalind_data_path, "r") as file:
    test_protein = file.read().strip()

with open(mass_table_path, "r") as file:
    mass_table = file.read().splitlines()
    mass_table = [line.split() for line in mass_table]
    mass_table = {line[0]: float(line[1]) for line in mass_table}

total_mass = 0
for protein_residue in test_protein:
    total_mass += mass_table[protein_residue]

print(total_mass)
