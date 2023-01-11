def count_dna_nucleotides(dna):
    """Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s"""
    acgt_counts = [dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')]
    print(*acgt_counts)


def transcribe(dna):
    """Given: A DNA string t
    Return: The transcribed RNA string of t"""
    return dna.replace('T', 'U')
