import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from wchain import compute_max_chain

class TestWChain(unittest.TestCase):
    def test_example_1(self):
        words = ["a", "ba", "bca", "bdca"]
        self.assertEqual(compute_max_chain(words), 4)

    def test_no_chain(self):
        words = ["a", "b", "c"]
        self.assertEqual(compute_max_chain(words), 1)

    def test_single_word(self):
        self.assertEqual(compute_max_chain(["hello"]), 1)

    def test_chain_with_duplicates(self):
        words = ["a", "ba", "bca", "bca", "bdca"]
        self.assertEqual(compute_max_chain(words), 4)

    def test_long_chain(self):
        words = ["a", "ab", "abc", "abcd", "abcde"]
        self.assertEqual(compute_max_chain(words), 5)


if __name__ == "__main__":
    unittest.main()
