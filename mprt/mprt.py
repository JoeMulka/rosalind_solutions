import requests
import xml.etree.ElementTree as ET
import regex as re


# Grab the XML data for this protein from uniprot
def get_protein_data(access_id, namespace):
    base_url = "https://rest.uniprot.org/uniprotkb/"
    full_url = base_url + access_id + ".xml"

    response = requests.get(full_url)
    xml_content = response.content
    ET.register_namespace("", namespace)
    root = ET.fromstring(xml_content)

    return root


def find_indices(pattern, text):
    # There are instances in the test data where the motifs overlap, so we use regex instead of re here
    # to get a version of finditer with an overlapped arg
    matches = re.finditer(pattern, text, overlapped=True)
    indices = [(match.start(), match.end()) for match in matches]
    return indices


# Rosalind is giving some access ids with the protein name appended to them, this removes that and
# returns just the access id
def fix_access_id(access_id):
    first_underscore_index = access_id.find("_")
    if first_underscore_index > 0:
        fixed_id = access_id[:first_underscore_index]
        return fixed_id
    else:
        return access_id


# Find all motif matches for a given motif and protein
def find_motif_matches(pattern, access_id):
    namespace = "http://uniprot.org/uniprot"
    root = get_protein_data(access_id, namespace)
    if root is None:
        print(f"data not found for access id: {access_id}")
    tree = ET.ElementTree(root)
    # For testing
    if False:
        ET.indent(tree, space="\t", level=0)
        tree.write("xml_test.xml", encoding="utf-8")
        name_xpath = f".//{{{namespace}}}protein/{{{namespace}}}recommendedName/{{{namespace}}}fullName"
        if root.find(name_xpath) is not None:
            protein_name = root.find(name_xpath).text
            print(protein_name)
        else:
            print("protein name not found")
    # Get the protein sequence
    sequence_xpath = f".//{{{namespace}}}sequence"
    protein_seq_list = root.findall(sequence_xpath)
    # This loop is necessary because for some proteins the XML had multiple <sequence> elements but only one has the sequence in it
    protein_seq = None
    for sequence_element in protein_seq_list:
        if sequence_element.text is not None:
            protein_seq = sequence_element.text
    if protein_seq is None:
        print(f"sequence not found for access_id {access_id}")
        return None

    if protein_seq == None:
        print(f"sequence field for access id {access_id} was empty")

    # Get the starting indices of all matches of the motif
    motif_locs = find_indices(pattern, protein_seq)

    # Rosalind wants the indices to be 1 indexed rather than 0 indexed
    one_indexed_starts = [str(match[0] + 1) for match in motif_locs]
    return one_indexed_starts


if __name__ == "__main__":
    target_motif = r"N[^P][ST][^P]"

    with open("rosalind_mprt.txt", "r") as infile:
        access_id_list = [line.strip() for line in infile]

    for access_id in access_id_list:
        one_indexed_starts = find_motif_matches(target_motif, fix_access_id(access_id))
        if one_indexed_starts:
            print(access_id)
            print(" ".join(one_indexed_starts))
