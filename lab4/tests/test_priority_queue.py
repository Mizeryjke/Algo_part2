import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_insert_and_peek(self):
        pq = PriorityQueue()
        pq.insert("low", 1)
        pq.insert("medium", 5)
        pq.insert("high", 10)
        self.assertEqual(pq.peek(), "high")

    def test_extract_max(self):
        pq = PriorityQueue()
        pq.insert("task1", 2)
        pq.insert("task2", 3)
        pq.insert("task3", 1)
        self.assertEqual(pq.extract_max(), "task2")
        self.assertEqual(pq.extract_max(), "task1")
        self.assertEqual(pq.extract_max(), "task3")
        self.assertIsNone(pq.extract_max())

    def test_equal_priority(self):
        pq = PriorityQueue()
        pq.insert("a", 5)
        pq.insert("b", 5)
        pq.insert("c", 5)
        self.assertIn(pq.extract_max(), {"a", "b", "c"})

if __name__ == "__main__":
    unittest.main()
