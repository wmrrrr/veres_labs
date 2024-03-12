import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.love import *

class TestFindTripletSum(unittest.TestCase):
    def test1(self):
        our_list = [30, 21, 45, 89, 5, 7, 3, 9, 1]
        target = 56
        expected_result = True
        self.assertEqual(find_triplet_sum(our_list, target), expected_result)

    def test2(self):
        our_list =[20, 40, 88, 6, 8, 33, 9, 5, 4, 50]
        target = 1
        expected_result = False
        self.assertEqual(find_triplet_sum(our_list, target), expected_result)

    def test3(self):
        our_list = [1, 10, 44, 3, 8, 22, 54, 9, 2, 80]
        target = 58
        expected_result = True
        self.assertEqual(find_triplet_sum(our_list, target), expected_result)

    def test4(self):
        our_list = [1, 10, 44, 3, 8, 22, 54, 9, 2, 80]
        target = 92
        expected_result = True
        self.assertEqual(find_triplet_sum(our_list, target), expected_result)        

    
if __name__ == '__main__':
    unittest.main()