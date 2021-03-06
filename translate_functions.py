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


def amino_codons_rna():
    """Returns a dictionary with codons and amino acids."""
    return {
        "UUU": "F",  	"CUU": "L",  	"AUU": "I",  	"GUU": "V",
        "UUC": "F",  	"CUC": "L",  	"AUC": "I",  	"GUC": "V",
        "UUA": "L",  	"CUA": "L",  	"AUA": "I",  	"GUA": "V",
        "UUG": "L",  	"CUG": "L",  	"AUG": "M",  	"GUG": "V",
        "UCU": "S",  	"CCU": "P",  	"ACU": "T",  	"GCU": "A",
        "UCC": "S",  	"CCC": "P",  	"ACC": "T",  	"GCC": "A",
        "UCA": "S",  	"CCA": "P",  	"ACA": "T",  	"GCA": "A",
        "UCG": "S",     "CCG": "P",  	"ACG": "T",  	"GCG": "A",
        "UAU": "Y",     "CAU": "H",  	"AAU": "N",  	"GAU": "D",
        "UAC": "Y",     "CAC": "H",  	"AAC": "N",  	"GAC": "D",
        "UAA": "Stop",	"CAA": "Q",	    "AAA": "K",  	"GAA": "E",
        "UAG": "Stop",	"CAG": "Q",  	"AAG": "K",  	"GAG": "E",
        "UGU": "C",  	"CGU": "R",  	"AGU": "S",  	"GGU": "G",
        "UGC": "C",	    "CGC": "R",     "AGC": "S",  	"GGC": "G",
        "UGA": "Stop",	"CGA": "R",	    "AGA": "R",  	"GGA": "G",
        "UGG": "W",  	"CGG": "R",  	"AGG": "R",  	"GGG": "G"
    }


def translator(frames: list):
    """Takes a list of open reading frames and translates each to all
    possible protein sequences, then returns these proteins in a nested
    list.

    Input:  frames - list, list with open reading frames.

    Output: Protein_list - nested list with all possible protein
                            sequences.
    """

    protein_list = []
    codon_dict = amino_codons_dna()

    # Iterates over the list with open reading frames.
    for frame in frames:
        frame_protein = []
        # Iterates over the reading frame.
        for counter, startcodon in enumerate(frame):
            # If a startcodon is found iterates over the rest of the
            # frame until a stopcodon is found.
            if codon_dict[startcodon] == "M":
                protein = []
                # Iterates over the frame from the point the start codon
                # is found.
                for codon in frame[counter:]:
                    amino = codon_dict[codon]
                    # If the amino acid != "Stop" it is added to
                    # protein.
                    if amino != "Stop":
                        protein.append(amino)
                    # If the amino acid == "Stop" the protein is added
                    # to frame_protein and the loop is broken.
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


def translator2(frames: list, seq_type: str):
    """Neemt een lijst met reading frames en berekend voor elke reading
    frame alle mogelijke eiwitten. Deze eiwitten worden toegevoegd aan
    een dictionary.

    Input:  frames - list, lijst met reading frames ieder bestaande uit
                            een lijst met codons.
            seq_type - str, 'RNA' of 'DNA' type van de sequenite.

    Output: frame_dict - dict, dictionary met frames als key en een
                                lijst met eiwitten als values.
    """
    # TODO wat te doen als geen stopcodon.
    if seq_type == "DNA":
        codon_dict = amino_codons_dna()
    else:
        codon_dict = amino_codons_rna()
    frame_dict = {}

    for num, frame in enumerate(frames):
        protein_list = []
        level = 0
        current_proteins = []
        part_prot = []
        # Itereert over het frame.
        for codon in frame:
            # Zoekt op welk aminozuur bij het codon hoort.
            amino = codon_dict[codon]
            if amino == "M":
                # Voegt 1 toe aan level (indentation voor html).
                level += 1
                if current_proteins:
                    # Voegt nieuw deel toe aan ider eiwit dat nu actief
                    # is.
                    for cur_prot in current_proteins:
                        cur_prot[1].extend(part_prot)
                # Begin nieuwe deeleiwit.
                part_prot = ["M"]
                current_proteins.append([level, []])
            elif amino == "Stop":
                if current_proteins:
                    # Voegt actieve eiwitten toe aan protein_list.
                    for cur_prot in current_proteins:
                        cur_prot[1].extend(part_prot)
                        protein_list.append((cur_prot[0],
                                             "".join(cur_prot[1])))
                # Reset level en actieve eiwitten.
                part_prot = []
                current_proteins = []
                level = 0
            elif part_prot:
                # Voegt amino to aan deeleiwit.
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
    """Kijkt of een sequentie DNA, RNA of geen van beiden is."""
    if not re.search(r"[^ATCG]", seq):
        return "DNA"
    elif not re.search(r"[^AUGC]", seq):
        return "RNA"
    else:
        return None


def get_translations(seq: str):
    """Neemt een sequentie, verdeeld deze in reading frames.
    Vervolgens worden alle mogelijke eiwitten berekend.

    Input:  seq - str, RNA sequentie

    Output: prot_dict - dict, dictionary met frames en eiwitsequenties.
    """
    seq = seq.upper()
    seq_type = check_dna(seq)
    frames = reading_frames(seq)
    prot_dict = translator2(frames, seq_type)
    return prot_dict
