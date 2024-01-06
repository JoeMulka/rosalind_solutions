from Bio import SeqIO

data_path = "rosalind_filt.fastq"
quality_threshold = 19
percent_bases_needed = 0.73

# 19 73

num_passed_sequences = 0
with open(data_path,"r") as input_handle:
    for record in SeqIO.parse(input_handle,"fastq"):
        quality_scores = record.letter_annotations["phred_quality"]
        bases_passed = sum([score >= quality_threshold for score in quality_scores])
        percent_passed = bases_passed / len(quality_scores)
        #print(percent_passed)
        if percent_passed >= percent_bases_needed:
            num_passed_sequences += 1
print(f"Number of sequences with more than {percent_bases_needed * 100}% bases over quality threshold {quality_threshold}: {num_passed_sequences}")
