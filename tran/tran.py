from Bio import SeqIO

purines = ["A","G"]
pyramidines = ["T","C"]
base_type_dict = {"A":"purine","G":"purine","T":"pyramidine","C":"pyramidine"}

sequences = []
with open("rosalind_tran.txt","r") as infile:
    for record in SeqIO.parse(infile, "fasta"):
        sequences.append(record)
print(sequences)

seq_1 = sequences[0]
seq_2 = sequences[1]


transition_count = 0
transversion_count = 0
for i in range(0,len(sequences[0])):
    if seq_1[i] == seq_2[i]:
        continue
    else:
        if base_type_dict[seq_1[i]] != base_type_dict[seq_2[i]]:
            transversion_count += 1
        else:
            transition_count += 1

print(f"transition count: {transition_count}")
print(f"transversion count: {transversion_count}")

ratio = transition_count/transversion_count
print(f"transition/transversion ratio: {ratio}")