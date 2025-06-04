import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.tree import BinaryTree, branchSums


class TestBranchSums(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        self.assertEqual(branchSums(root), 24)

    def test_case_2_only_root(self):
        root = BinaryTree(10)
        self.assertEqual(branchSums(root), 0)

    def test_case_3_left_leaf_only(self):
        root = BinaryTree(5)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(1)
        self.assertEqual(branchSums(root), 1)


if __name__ == "__main__":
    unittest.main()