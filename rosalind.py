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


def gc_content(dna):
    """returns the gc content of a dna string as a percentage"""
    return (dna.count('G') + dna.count('C')) / len(dna) * 100


def hamming_distance(s, t):
    """Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t)."""
    assert(len(s) == len(t))
    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1
    return distance


codon_table = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G """


def translate(rna):
    codons = codon_table.split()
    protein = ""
    codon_lookup_table = dict(zip(codons[0::2], codons[1::2]))
    for n in range(0, len(rna) - 2, 3):
        codon = codon_lookup_table[rna[n:n+3]]
        if codon == "Stop":
            break
        else:
            protein += codon
    return protein

def motif_finding(s, t):
    """Given: Two DNA strings s and t
    Return: All locations of t as a substring of s."""
    locations = []
    motif_length = len(t)
    for i in range(0, len(s) - motif_length):
        if s[i:i+motif_length] == t:
            locations.append(i+1)
    return locations

