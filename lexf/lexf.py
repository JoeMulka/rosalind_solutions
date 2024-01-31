from itertools import permutations
from itertools import product

alphabet = "A B C D"

alphabet = alphabet.split()

string_length = 4

print(alphabet)


def score_string(target_string):
    # Assume that the order of the character in the element is its priority / intended sort order
    # Rosalind question doesn't actually need this as it is always using standard English order of symbols

    string_score = 0
    for i in range(1, len(target_string) + 1):
        char_score = alphabet.index(target_string[i - 1])
        string_score += (len(alphabet) ** (len(target_string) - i)) * char_score
    return string_score


# all_perms = permutations(alphabet, string_length)
all_perms = product(alphabet, repeat=string_length)
# all_perms = sorted(all_perms, key=score_string)
all_perms = sorted(all_perms)
all_perms = ["".join(perm) for perm in all_perms]
print("\n".join(all_perms))
