# Define the genetic code as a dictionary
genetic_code = {
    'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
    'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'Stop',
    'UAG': 'Stop', 'UGA': 'Stop', 'CUU': 'Leucine', 'CUC': 'Leucine',
    'CUA': 'Leucine', 'CUG': 'Leucine', 'CCU': 'Proline', 'CCC': 'Proline',
    'CCA': 'Proline', 'CCG': 'Proline', 'CAU': 'Histidine', 'CAC': 'Histidine',
    'CAA': 'Glutamine', 'CAG': 'Glutamine', 'CGU': 'Arginine', 'CGC': 'Arginine',
    'CGA': 'Arginine', 'CGG': 'Arginine', 'AUU': 'Isoleucine', 'AUC': 'Isoleucine',
    'AUA': 'Isoleucine', 'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine',
    'ACG': 'Threonine', 'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine',
    'AAG': 'Lysine', 'AGU': 'Serine', 'AGC': 'Serine', 'AGA': 'Arginine',
    'AGG': 'Arginine', 'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine',
    'GUG': 'Valine', 'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine',
    'GCG': 'Alanine', 'GAU': 'Aspartate', 'GAC': 'Aspartate', 'GAA': 'Glutamate',
    'GAG': 'Glutamate', 'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine',
    'GGG': 'Glycine'
}

def map_gene_to_protein(sequence):
    # Ensure the sequence length is a multiple of 3
    if len(sequence) % 3 != 0:
        return "Invalid gene sequence. The length is not a multiple of 3."

    # Initialize the result as a list to hold the protein
    protein = []

    # Iterate through the sequence in steps of 3 nucleotides (a codon)
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]  # Extract codon
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            if amino_acid == 'Stop':  # Stop translation if a stop codon is found
                break
            protein.append(amino_acid)
        else:
            return f"Invalid codon found: {codon}"

    return protein

# Example usage
gene_sequence = "AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGA"
# Mapping the gene sequence to amino acids
result = map_gene_to_protein(gene_sequence)

# Output the result
print("Protein sequence:", result)
