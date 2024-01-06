from itertools import permutations
from math import perm

perm_length = 7

# This should be equivalent to factorial(perm_length)
num_permutations = perm(perm_length,perm_length)

all_permutations = permutations(range(1,perm_length+1))
with open("permutations.txt","w") as outfile:
    outfile.write(str(num_permutations) + "\n")
    for single_perm in all_permutations:
        outfile.write(" ".join([str(x) for x in single_perm]) + "\n")