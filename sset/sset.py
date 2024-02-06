# If we simply an SNP at any position to be binary, that is, the base is either mutated or isn't (rather than mutated to A, or mutated to B, etc.)
# Then we can draw a binary tree to represent arrangements of "on" and "off" for every base in the sequence
# If, instead of "On" for an SNP at position i, we instead make a set of indices that are on, then we have a set that is a subset of
# the list of possible indices
# We can make a binary tree starting with the empty set.  At each bifurcation, one branch recieves a mutation from the list of unmutated indices
# And the other does not.  When the indices are exhausted, one extreme leaf will have no SNPs, another will have all of them, and there is a leaf for
# every subset inbetween.  The height of the binary tree is equal to the length of the mutable sequence

n = 932

running_product = 1
for i in range(0, n):
    running_product *= 2
    running_product %= 1000000

print(running_product)
