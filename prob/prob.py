from Bio.Seq import Seq
from Bio.SeqUtils import GC
import math

test_seq = Seq("ACGATACAA")
test_gc_contents = "0.129 0.287 0.423 0.476 0.641 0.742 0.783".split()
test_gc_contents = [float(gc) for gc in test_gc_contents]

rosalind_seq = Seq(
    "CGCTTGCGGATAGAGAAAGTCTCCGCACGACGTGTTGCAGGTAACTATTAGGCGCCCAACCAGGTTATCCTTACCTGGTGGGGCCCACACAAGGC"
)
rosalind_gc_contents = "0.075 0.145 0.238 0.267 0.344 0.395 0.490 0.533 0.590 0.644 0.694 0.758 0.828 0.927".split()
rosalind_gc_contents = [float(gc) for gc in rosalind_gc_contents]

seq = rosalind_seq
gc_contents = rosalind_gc_contents

probability_random = []
for gc_content in gc_contents:
    running_log_sum = 0
    base_probabilites = {
        "G": gc_content / 2,
        "C": gc_content / 2,
        "A": (1 - gc_content) / 2,
        "T": (1 - gc_content) / 2,
    }
    for base in seq:
        running_log_sum += math.log10(base_probabilites[base])
    probability_random.append(running_log_sum)

# Round to 3 decimal places
probability_random = [str(round(prob, 3)) for prob in probability_random]

print(" ".join(probability_random))
