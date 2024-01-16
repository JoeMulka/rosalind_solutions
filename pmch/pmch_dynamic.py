""
#sequence = "AGCUAGUCAU"
#sequence = "AUGC"
sequence = "ACGAUCGUGACACGCUGGCUUCGGACCGUCGACUUACAGCCGUACUACGCAAUUGACUGGUAGCUACGUAGGAUGC"
match_dict = {"A":"U","U":"A","C":"G","G":"C"}
edges = []

def match_nodes(sequence):
    print(sequence)
    # Match with each possible partner, then spawn a recursive call on the sequence with those two bases removed
    if len(sequence) == 2:
        if match_dict[sequence[0]] == sequence[1]:
            return 1
        else:
            return 0
    num_perfect = 0

    for i,base in enumerate(sequence):
        if i != 0:
            if match_dict[sequence[0]] == base:
                first_half = sequence[1:i]
                second_half = sequence[i+1:]
                reduced_sequence = first_half + second_half
                num_perfect += match_nodes(reduced_sequence)
    return num_perfect

print(match_nodes(sequence))
