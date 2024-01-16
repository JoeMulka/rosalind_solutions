from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description="Convert fastq to fasta")
parser.add_argument(
    "--fastq-filepath", default="example.fastq", help="fastq file to convert"
)
parser.add_argument(
    "--fasta-filepath", default="example.fasta", help="fasta file to write to"
)
args = parser.parse_args()


with open(args.fastq_filepath, "r") as input_handle, open(
    args.fasta_filepath, "w"
) as output_handle:
    sequences = SeqIO.parse(input_handle, "fastq")
    count = SeqIO.write(sequences, output_handle, "fasta")

print("Converted %i records" % count)
