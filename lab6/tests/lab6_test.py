import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from lab6 import possible_pairs


class TestCountPossiblePairs(unittest.TestCase):
    def test_example1(self):
        n = 3
        pairs = [(1, 2), (2, 4), (3, 5)]
        result = possible_pairs(n, pairs)
        self.assertEqual(result, 4)

    def test_no_pairs(self):
        n = 0
        pairs = []
        result = possible_pairs(n, pairs)
        self.assertEqual(result, 0)
        
if __name__ == "__main__":
    unittest.main()
