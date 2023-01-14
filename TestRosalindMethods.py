import unittest
from rosalind import reverse_complement
from rosalind import transcribe
from rosalind import rabbits


class TestRosalindMethods(unittest.TestCase):
    # test expected, actual
    def test_transcribe(self):
        self.assertEqual(transcribe("GATGGAACTTGACTACGTAAATT"), 'GAUGGAACUUGACUACGUAAAUU')

    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("AAAACCCGGT"), "ACCGGGTTTT")

    def test_rabbits(self):
        self.assertEqual(19, rabbits(5, 3))


if __name__ == '__main__':
    unittest.main()
