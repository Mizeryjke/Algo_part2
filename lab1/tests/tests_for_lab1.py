import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lab1 import order


class Testing(unittest.TestCase):
    def test_plot_5x5(self):
        plot =[
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25], 
        ]
        expected = [5, 10, 15, 20, 25, 24, 19, 14, 9, 4, 3, 8, 13, 18, 23, 22, 17, 12, 7, 2, 1, 6, 11, 16, 21]
        self.assertEqual(order(plot), expected)
    
    def test_plot_2x4(self):
        plot = [ 
            [1, 2, 3, 4],
            [5, 6, 7, 8]  
            ]
        expected = [4, 8, 7, 3, 2, 6, 5, 1]
        self.assertEqual(order(plot), expected)
    
if __name__ == "__main__":
    unittest.main()
