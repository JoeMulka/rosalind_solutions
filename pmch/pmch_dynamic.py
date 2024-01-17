from multiprocessing import Pool
from itertools import starmap
import time

# sequence = "AGCUAGUCAU"
# sequence = "AUGC"
sequence = (
    "ACGAUCGUGACACGCUGGCUUCGGACCGUCGACUUACAGCCGUACUACGCAAUUGACUGGUAGCUACGUAGGAUGC"
)
match_dict = {"A": "U", "U": "A", "C": "G", "G": "C"}


def match_nodes(sequence, first_iteration):
    # Match with each possible partner, then spawn a recursive call on the sequence with those two bases removed
    if len(sequence) == 2:
        if match_dict[sequence[0]] == sequence[1]:
            return 1
        else:
            return 0
    # num_perfect = 0

    modified_strings = []
    for i, base in enumerate(sequence):
        if i != 0:
            if match_dict[sequence[0]] == base:
                first_half = sequence[1:i]
                second_half = sequence[i + 1 :]
                reduced_sequence = first_half + second_half
                # num_perfect += match_nodes(reduced_sequence)
                modified_strings.append(reduced_sequence)
    # print(modified_strings)
    if first_iteration:
        with Pool(processes=10) as my_pool:
            results_list = my_pool.starmap(
                match_nodes, [(seq, False) for seq in modified_strings]
            )
    else:
        results_list = starmap(match_nodes, [(seq, False) for seq in modified_strings])
    return sum(results_list)


start_time = time.time()
print(match_nodes(sequence, True))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time elapsed: {elapsed_time} second")
