import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.lab7 import naive_search_last

class TestNaiveSearchLast(unittest.TestCase):
    def test_found_once(self):
        haystack = "abracadabra"
        needle = "cada"
        index, comps = naive_search_last(haystack, needle)
        self.assertEqual(index, 7)
        self.assertTrue(comps > 0)


    def test_found_multiple(self):
        haystack = "banana bandana banana"
        needle = "ana"
        index, comps = naive_search_last(haystack, needle)
        self.assertEqual(index, 20)
        self.assertTrue(comps > 0)

    def test_not_found(self):
        haystack = "hello world"
        needle = "test"
        index, comps = naive_search_last(haystack, needle)
        self.assertEqual(index, -1)
        self.assertTrue(comps > 0)

    def test_empty_needle(self):
        haystack = "abc"
        needle = ""
        index, comps = naive_search_last(haystack, needle)
        self.assertEqual(index, -1)
        self.assertEqual(comps, 0)

if __name__ == "__main__":
    unittest.main()