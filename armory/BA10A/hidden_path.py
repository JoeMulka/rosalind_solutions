# https://rosalind.info/problems/ba10a/

transition_table = {
    "A": {"A": 0.334, "B": 0.666},
    "B": {"A": 0.452, "B": 0.548},
}

path = "ABAABBAABBABAABBAAABAABBBABABBAABBAAAAABAABBAAAAAA"

running_prob = 0.5
current_state = path[0]
for character in path[1:]:
    t_prob = transition_table[current_state][character]
    running_prob *= t_prob
    current_state = character

print(running_prob)
