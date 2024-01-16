import os

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "4_rosalind_fib.txt")

# Check if data path file exists
if os.path.exists(data_path):
    with open(data_path, "r") as infile:
        input_data = infile.read()
        input_data = input_data.split()


else:
    sample = [5, 3]
    input_data = sample

n = int(input_data[0])
k = int(input_data[1])

# This is actually gen 0
fib_sequence = [1]

for gen in range(1, n):
    if len(fib_sequence) < 2:
        fib_sequence.append(1)
    else:
        fib_sequence.append(fib_sequence[gen - 1] + (k * fib_sequence[gen - 2]))

print(fib_sequence)
