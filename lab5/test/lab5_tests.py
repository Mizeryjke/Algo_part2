import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab5 import find_root

class TestLab5(unittest.TestCase):

    def test_graph_strongly_connected(self):
        graph = {
            0: [1, 2],
            1: [2, 3],
            2: [0, 4],
            3: [4],
            4: [2, 3]
        }
        self.assertIn(find_root(graph), [0, 1, 2, 3, 4])

    def test_graph_with_root(self):
        graph = {
            0: [1],
            1: [2],
            2: [3],
            3: [0],
            4: [3],
            5: [0]
        }
        self.assertEqual(find_root(graph), -1)  # бо 5 ізольований

    def test_graph_no_root(self):
        graph = {
            0: [1],
            1: [],
            2: [0]
        }
        self.assertEqual(find_root(graph), 2)  # бо 2 → 0 → 1

if __name__ == '__main__':
    unittest.main()
