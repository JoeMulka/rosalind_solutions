from Bio import SeqIO
from Bio.Seq import Seq


# Function for returning a codon
def codon_generator(sequence):
    for i in range(0, len(sequence), 3):
        yield sequence[i : i + 3]


def search_for_orfs(sequence, offset):
    direction_orfs = []
    # Get chunks of three bases at a time
    codon_list = list(codon_generator(sequence))
    for codon_index, codon in enumerate(codon_list):
        if len(codon) < 3:
            # We've reached the end of the sequence, and have gotten a partial codon
            break
        protein = codon.translate()
        if protein == "M":
            # Start a new ORF
            orf = Seq("M")
            for codon in codon_list[codon_index + 1 :]:
                protein = codon.translate()
                if protein == "*":
                    # Stop codon
                    direction_orfs.append(orf)
                    break
                if protein == "M":
                    # Found a new ORF within this one
                    sequence_index = (codon_index * 3) + 1
                    direction_orfs += search_for_orfs(sequence[sequence_index:], 0)
                    orf += protein
                else:
                    orf += protein

    return direction_orfs


if __name__ == "__main__":
    test_path = "test_data.fasta"
    rosalind_path = "rosalind_orf.txt"

    with open(rosalind_path, "r") as f:
        records = list(SeqIO.parse(f, "fasta"))

    forward_sequence = records[0].seq
    all_forward_orfs = []
    all_reverse_orfs = []
    for offset in range(0, 3):
        this_offset_forward_orfs = search_for_orfs(forward_sequence[offset:], offset)
        this_offset_reverse_orfs = search_for_orfs(
            forward_sequence.reverse_complement()[offset:], offset
        )
        if this_offset_forward_orfs:
            all_forward_orfs += this_offset_forward_orfs
        if this_offset_reverse_orfs:
            all_reverse_orfs += this_offset_reverse_orfs

    all_orfs = all_forward_orfs + all_reverse_orfs
    all_orfs = set([str(orf) for orf in all_orfs])
    print("\n".join(all_orfs))
