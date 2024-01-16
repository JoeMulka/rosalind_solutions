import os

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "7_rosalind_iprb.txt")

# Check if data path file exists
if os.path.exists(data_path):
    with open(data_path, "r") as infile:
        input = infile.read()
        input_strings = input.split()
        homo_dominant, hetero, homo_recessive = [int(x) for x in input_strings]
else:
    homo_dominant, hetero, homo_recessive = 2, 2, 2

total = homo_dominant + hetero + homo_recessive

# Need to calculate probability of each of getting at least one dominant allele
# Do this by finding inverse probability of getting no dominant alleles (double recessive)

# Probability of the three selection events that lead to a double recessive phenotype
p_both_homo_recessive = (homo_recessive / total) * ((homo_recessive - 1) / (total - 1))
p_one_hetero = ((2 * hetero * homo_recessive) / (total * (total - 1))) * 0.5
p_both_hetero = ((hetero / total) * ((hetero - 1) / (total - 1))) * 0.25

p_child_homo_recessive = p_both_homo_recessive + p_one_hetero + p_both_hetero
p_child_min1_dominant = 1 - p_child_homo_recessive

print(
    "Probability that child has at least one dominant allele: {}".format(
        p_child_min1_dominant
    )
)
