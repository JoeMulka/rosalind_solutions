from Bio import SeqIO
import time
import os


# This does the check by starting with the longest possible match and reducing its length
# This allows the python code to match the definition of the test and prefix strings in the question
# But it also runs very slowly on long sequences
def brute_force_mode(sequence):
    failure_sequence = [0] * len(sequence)
    # figure out the value of P(k)
    for k in range(1, len(failure_sequence)):
        match_length = 0
        for j in range(1, k):
            prefix_seq = sequence[0 : k - j]
            test_seq = sequence[j:k]
            if len(test_seq) != len(prefix_seq):
                print(f"length of test seq: {len(test_seq)}")
                print(f"length of prefix seq: {len(prefix_seq)}\n")
            if test_seq == prefix_seq:
                match_length = len(test_seq)
                break
        failure_sequence[k - 1] = match_length
    return failure_sequence


def turbo_mode(sequence):
    failure_sequence = [0] * len(sequence)
    match_length = 0

    for k in range(1, len(failure_sequence)):
        # The possible match lengths for a given k are 0 through the match length immediately before it, plus 1
        match_length = failure_sequence[k - 1]
        for potential_length in range(match_length + 1, 0, -1):
            test_seq = sequence[k - potential_length + 1 : k + 1]
            prefix_seq = sequence[0 : len(test_seq)]

            if len(test_seq) != len(prefix_seq):
                print(f"length of test seq: {len(test_seq)}")
                print(f"length of prefix seq: {len(prefix_seq)}\n")

            if test_seq == prefix_seq:
                match_length += 1
                failure_sequence[k] = len(test_seq)
                break
            elif test_seq != prefix_seq:
                if failure_sequence[k] > 0:
                    break
    return failure_sequence


if __name__ == "__main__":

    workdir = "/home/joe/dev/rosalind_solutions/kmp"
    sample_data = "sample_data.fasta"
    rosalind_data = "rosalind_kmp.txt"
    outfile = "kmp_output.txt"
    brute_force = False

    with open(os.path.join(workdir, rosalind_data), "r") as infile:
        sequence = SeqIO.read(infile, "fasta")

    # Run the fast failue sequence algorithm
    turbo_start_time = time.time()
    failure_sequence = turbo_mode(sequence.seq)
    turbo_end_time = time.time()
    elapsed = turbo_end_time - turbo_start_time
    print(f"Turbo mode took {elapsed:.4f} seconds")
    failure_sequence = [str(x) for x in failure_sequence]
    # print(" ".join(failure_sequence))

    # Write the output to a file
    with open(os.path.join(workdir, outfile), "w") as out:
        out.write(" ".join(failure_sequence) + "\n")

    # Run the brute force algorithm if comparing runtime on a given sequence
    if brute_force:
        brute_force_start_time = time.time()
        brute_failure_sequence = brute_force(sequence.seq)
        brute_force_end_time = time.time()
        print(
            f"Brute force mode took {brute_force_end_time - brute_force_start_time} seconds"
        )
