import unittest
from rosalind import reverse_complement
from rosalind import transcribe
from rosalind import rabbits
from rosalind import gc_content
from rosalind import hamming_distance
from rosalind import translate
from Bio import SeqIO



class TestRosalindMethods(unittest.TestCase):
    # test expected, actual
    def test_transcribe(self):
        self.assertEqual(transcribe("GATGGAACTTGACTACGTAAATT"), 'GAUGGAACUUGACUACGUAAAUU')

    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("AAAACCCGGT"), "ACCGGGTTTT")

    def test_rabbits(self):
        self.assertEqual(19, rabbits(5, 3))

    def test_gc_content(self):
        max = 0
        with open("gc_content.fasta") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                gc = gc_content(record)
                if gc > max:
                    max = gc
        self.assertAlmostEqual(60.919540, max, delta=0.001)

    def test_hamming_distance(self):
        with open("hamming_distance.txt") as file:
            s = file.readline().strip()
            t = file.readline().strip()
            self.assertEqual(7, hamming_distance(s, t))

    def test_translate(self):
        self.assertEqual("MAMAPRTEINSTRING", translate("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))


if __name__ == '__main__':
    unittest.main()
