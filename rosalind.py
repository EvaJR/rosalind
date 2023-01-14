def count_dna_nucleotides(dna):
    """Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s"""
    acgt_counts = [dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')]
    print(*acgt_counts)


def transcribe(dna):
    """Given: A DNA string t
    Return: The transcribed RNA string of t"""
    return dna.replace('T', 'U')


def reverse_complement(dna):
    """Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s."""
    complement = ""
    for nucleotide in dna:
        if nucleotide == "A":
            complement += "T"
        elif nucleotide == "T":
            complement += "A"
        elif nucleotide == "C":
            complement += "G"
        elif nucleotide == "G":
            complement += "C"
    return complement[::-1]


def rabbits(n, k):
    """Return: The total number of rabbit pairs that will be present after n months,
    if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
    rabbit pairs (instead of only 1 pair)."""
    rabbits = [1, 1]
    while len(rabbits) < n:
        rabbits.append(rabbits[-1] + rabbits[-2] * k)
    return rabbits[-1]

