import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.love import *

class Test(unittest.TestCase):
    def test1(self):
        our_list = (1, 2, 3, 4, 6)
        left = 0
        right = len(our_list) - 1
        target = 6
        expected_result = True
        self.assertEqual(binary_search(our_list, left, right, target), expected_result)

    def test2(self):
        our_list = (1, 2, 3, 4, 6, 7, 9, 10, 5, 8)
        left = 0
        right = len(our_list) - 1
        target = 6
        expected_result = True
        self.assertEqual(binary_search(our_list, left, right, target), expected_result)

    def test3(self):
        our_list = (7, 8, 9, 10)
        left = 0
        right = len(our_list) - 1
        target = 6
        expected_result = False
        self.assertEqual(binary_search(our_list, left, right, target), expected_result)

    def test4(self):
        our_list = (1, 4, 10, 2, 3, 9)
        left = 0
        right = len(our_list) - 1
        target = 6
        expected_result = False
        self.assertEqual(binary_search(our_list, left, right, target), expected_result)        

    
if __name__ == '__main__':
    unittest.main()