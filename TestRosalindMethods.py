import unittest
from rosalind import reverse_complement
from rosalind import transcribe


class TestRosalindMethods(unittest.TestCase):

    def test_transcribe(self):
        self.assertEqual(transcribe("GATGGAACTTGACTACGTAAATT"), 'GAUGGAACUUGACUACGUAAAUU')

    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("AAAACCCGGT"), "ACCGGGTTTT")


if __name__ == '__main__':
    unittest.main()
