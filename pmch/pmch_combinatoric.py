from collections import Counter
from math import factorial

# sequence = "AUGC"
sequence = "UUUGCCUUACGAAGGUCGACUCGGAUUGUGGCAAAGUCGCCCUUCAAUUUAGAUAGAAACUAAAGCCGCCUGGC"

# sequence = "AGCUAGUCAU"

base_counts = Counter(sequence)

print(base_counts)
num_matches = factorial(base_counts["A"]) * factorial(base_counts["C"])
print(num_matches)
