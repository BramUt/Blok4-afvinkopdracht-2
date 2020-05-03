import re

def amino_codons_dna():
    """Returns a dictionary with codons and amino acids."""
    return {
        "TTT": "F",     "CTT": "L",     "ATT": "I",     "GTT": "V",
        "TTC": "F",     "CTC": "L",     "ATC": "I",     "GTC": "V",
        "TTA": "L",     "CTA": "L",     "ATA": "I",     "GTA": "V",
        "TTG": "L",     "CTG": "L",     "ATG": "M",     "GTG": "V",
        "TCT": "S",     "CCT": "P",     "ACT": "T",     "GCT": "A",
        "TCC": "S",     "CCC": "P",     "ACC": "T",     "GCC": "A",
        "TCA": "S",     "CCA": "P",     "ACA": "T",     "GCA": "A",
        "TCG": "S",     "CCG": "P",     "ACG": "T",     "GCG": "A",
        "TAT": "Y",     "CAT": "H",     "AAT": "N",     "GAT": "D",
        "TAC": "Y",     "CAC": "H",     "AAC": "N",     "GAC": "D",
        "TAA": "Stop",  "CAA": "Q",     "AAA": "K",     "GAA": "E",
        "TAG": "Stop",  "CAG": "Q",     "AAG": "K",     "GAG": "E",
        "TGT": "C",     "CGT": "R",     "AGT": "S",     "GGT": "G",
        "TGC": "C",     "CGC": "R",     "AGC": "S",     "GGC": "G",
        "TGA": "Stop",  "CGA": "R",     "AGA": "R",     "GGA": "G",
        "TGG": "W",     "CGG": "R",     "AGG": "R",     "GGG": "G"
        }


def translator(frames: list):
    """Takes a list of open reading frames and translates each to all possible
    protein sequences, then returns these proteins in a nested list.

    Input:  frames - list, list with open reading frames.

    Output: Protein_list - nested list with all possible protein sequences.
    """

    protein_list = []
    codon_dict = amino_codons_dna()

    # Iterates over the list with open reading frames.
    for frame in frames:
        frame_protein = []
        # Iterates over the reading frame.
        for counter, startcodon in enumerate(frame):
            # If a startcodon is found iterates over the rest of the frame
            # until a stopcodon is found.
            if codon_dict[startcodon] == "M":
                protein = []
                # Iterates over the frame from the point the start codon is
                # found.
                for codon in frame[counter:]:
                    amino = codon_dict[codon]
                    # If the amino acid != "Stop" it is added to protein.
                    if amino != "Stop":
                        protein.append(amino)
                    # If the amino acid == "Stop" the protein is added to
                    # frame_protein and the loop is broken.
                    if amino == "Stop":
                        frame_protein.append("".join(protein))
                        break
        # If any protein are found these are added to protein_list.
        if frame_protein:
            protein_list.append(frame_protein)
        # If none are found a list with just a string "None" is added to
        # protein_list.
        else:
            protein_list.append(["None"])

    prot1, prot2, prot3 = protein_list

    return {"frame1": prot1, "frame2": prot2,
            "frame3": prot3}


def translator2(frames: list):
    # TODO wat te doen als geen stopcodon.
    codon_dict = amino_codons_dna()
    frame_dict = {}

    for num, frame in enumerate(frames):
        protein_list = []
        level = 0
        current_proteins = []
        part_prot = []
        for codon in frame:
            amino = codon_dict[codon]
            if amino == "M":
                level += 1
                if current_proteins:
                    for cur_prot in current_proteins:
                        cur_prot[1].extend(part_prot)
                part_prot = ["M"]
                current_proteins.append([level, []])
            elif amino == "Stop":
                if current_proteins:
                    for cur_prot in current_proteins:
                        cur_prot[1].extend(part_prot)
                        protein_list.append((cur_prot[0],
                                             "".join(cur_prot[1])))
                part_prot = []
                current_proteins = []
                level = 0
            elif part_prot:
                part_prot.append(amino)

        frame_dict[f"frame{num+1}"] = protein_list

    return frame_dict


def reading_frames(seq: str):
    """Takes a DNA/RNA sequence and returns the 3 corresponding reading frames
    in a list.

    Input:  seq - str , DNA/RNA sequece

    Output: frames - list, list with 3 open reading frames.
    """
    seq = re.sub(r"\s+", "", seq)
    frames = []

    # Iterates over seq and makes 3 lists containing a reading frame each.
    for i in range(3):
        frame = []
        # Splits the sequence in base triplets.
        for j in range(i, len(seq), 3):
            # Adds a part of seq to the frame if it's 3 characters long.
            if len(seq[j:j+3]) == 3:
                frame.append(seq[j:j+3])
        frames.append(frame)

    return frames


def check_dna(seq: str):

    if not re.search(r"[^ATCG]", seq):
        return "DNA"
    elif not re.search(r"[^AUGC]", seq):
        return "RNA"
    else:
        return None


def get_translations(seq: str):
    seq = seq.upper()
    if seq_type := check_dna(seq):
        print(seq_type)

    frames = reading_frames(seq)
    prot_dict = translator2(frames)
    return prot_dict
