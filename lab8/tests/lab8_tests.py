import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from lab8 import compute_max_flow

class TestMaxFlow(unittest.TestCase):
    def setUp(self):
        self.filename = os.path.join(os.path.dirname(__file__), "..", "roads.csv")

    def test_max_flow(self):
        result = compute_max_flow(self.filename)
        self.assertEqual(result, 35)

if __name__ == "__main__":
    unittest.main()
