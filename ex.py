                               # A program for mapping a gene in the genetic code

# A CODON IS BASICALLY A SEQUENCE OF 3 DNA OR RNA BASES.
# EACH OF THE SEQUENCE CORRESPOND TO SPECIFIC AMINO ACID.
# START CODON SIGNALS THE RIBOSOME TO START SYNTHESISING THE PROTEIN
# STOP CODON SIGNALS THE RIBOSOME TO STOP SYNTHESISING THE PROTEIN
# THE TRANSLATION HAS 3 PHASES: INTIATION, ELONGATION AND TERMINATION

# Genetic code dictionary to map codons to amino acids
# The inforamtion of the genetic code is store in the form of base pairs which are;
# Adenine, Cytosine, Guanine, Thymine (Uracil)
genetic_code = {
    'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
    'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'CUU': 'Leucine',
    'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine', 'CCU': 'Proline',
    'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline', 'CAU': 'Histidine',
    'CAC': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine', 'CGU': 'Arginine',
    'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine', 'AUU': 'Isoleucine',
    'AUC': 'Isoleucine', 'AUA': 'Isoleucine', 'ACU': 'Threonine', 'ACC': 'Threonine',
    'ACA': 'Threonine', 'ACG': 'Threonine', 'AAU': 'Asparagine', 'AAC': 'Asparagine',
    'AAA': 'Lysine', 'AAG': 'Lysine', 'AGU': 'Serine', 'AGC': 'Serine',
    'AGA': 'Arginine', 'AGG': 'Arginine', 'GUU': 'Valine', 'GUC': 'Valine',
    'GUA': 'Valine', 'GUG': 'Valine', 'GCU': 'Alanine', 'GCC': 'Alanine',
    'GCA': 'Alanine', 'GCG': 'Alanine', 'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid',
    'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid', 'GGU': 'Glycine', 'GGC': 'Glycine',
    'GGA': 'Glycine', 'GGG': 'Glycine'
}

# Function to translate RNA sequence to protein
def translate_rna_to_protein(rna_sequence):
    start_codon = 'AUG' #Define the start codon, which signals the beginning of translation
    stop_codons = {'UAA', 'UAG', 'UGA'} # Define the stop codon, which signals the end of translation
    
    protein = []  # list to hold the translated amino acids (protein)

 # Find the poition of the start codon in the RNA sequence which 
 # the translation will begin from the first occurence 'AUG'
    start_index = rna_sequence.find(start_codon)
    
    if start_index == -1: # If no start codon is found, return a message
        return "Start codon not found."

# Loop through the RNA in steps of 3 nucleotides (1 codon) 
    for i in range(start_index, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3] # extract a codon from the RNA sequence
        if codon in stop_codons: # stop translation
            break
        if codon in genetic_code: #if the codon exists in the genetic code, add the corrrsponding amino acid to the protein list
            protein.append(genetic_code[codon])
        else:
            protein.append('Unknown')

    return protein

# Sample RNA sequence
rna_sequence = 'AUGUUUUUC'

# Translate RNA to protein
protein = translate_rna_to_protein(rna_sequence)

print("Protein sequence:", protein)
