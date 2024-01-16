from Bio import SeqIO
data_path = "rosalind_revp.txt"
out_path = "output.txt"

with open(data_path,"r") as infile:
    sequence = next(SeqIO.parse(infile,"fasta"))

window_sizes = range(4,13)

with open(out_path,"w") as outfile:
    for size in window_sizes:
        for i in range(0,len(sequence.seq) - size + 1):
            seq_slice = sequence[0+i:size+i]
            if seq_slice.seq == seq_slice.reverse_complement().seq:
                outfile.write(f"{i+1} {size}\n")
                print(f"{i+1} {size}")
                #print(seq_slice.seq)