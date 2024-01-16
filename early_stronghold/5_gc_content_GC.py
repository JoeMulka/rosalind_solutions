import os

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "5_rosalind_gc.txt")


class FastARecord:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def calculate_gc_content(self):
        gc_count = 0
        for base in self.sequence:
            if base in ["G", "C"]:
                gc_count += 1
        # Format as percent
        return (gc_count / len(self.sequence)) * 100


def ingest_fasta(data_path):
    """Returns a generator that yields FastARecord objects from a FastA file"""
    with open(data_path, "r") as infile:
        first_line = True
        for line in infile.readlines():
            if line.startswith(">"):
                if not first_line:
                    # A > indicates the end of an entry and the start of a new one, except for the very first one in the file
                    yield FastARecord(name, sequence)
                else:
                    # If we reach this point, we are on the first line of the file.  Set first_line to False to indicate we are no longer on the first line
                    first_line = False
                # remove the > from the name
                name = line.strip()[1:]
                # Start a new sequence
                sequence = ""
            else:
                # We are in the middle of a sequence, add this line to the growing sequence
                sequence += line.strip()
        yield FastARecord(name, sequence)


if __name__ == "__main__":
    # Check if data path file exists
    if os.path.exists(data_path):
        highest_content = 0
        highest_name = ""

        fasta_files = ingest_fasta(data_path)
        for fasta_file in fasta_files:
            if fasta_file.calculate_gc_content() > highest_content:
                highest_content = fasta_file.calculate_gc_content()
                highest_name = fasta_file.name
        print(highest_name)
        print(highest_content)

    else:
        print("filename invalid")
