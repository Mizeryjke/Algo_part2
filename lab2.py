import unittest
from tests_for_lab2 import sum_in_massive


class TestThreeSum(unittest.TestCase):
    def test_massive_1(self):
        self.assertTrue(sum_in_massive([1, 2, 3], 6))

    def test_massive_2(self):
        self.assertFalse(sum_in_massive([1, 2, 4], 6))

    def test_massive_5(self):
        self.assertTrue(sum_in_massive([90, 10, 150, 200,150], 300))



if __name__ == "__main__":
    unittest.main()
