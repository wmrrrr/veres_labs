import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.road import route

class TestElements(unittest.TestCase):
    def test_similar_elements(self):
        our_list = [[1, 2, 3], [3, 5, 7], [4, 3, 5]]
        expected_result = [1, 2, 3, 7, 5, 3, 4, 3, 5]
        self.assertEqual(route(our_list), expected_result)

    def test_counter(self):
        our_list = [[3,4,5,1],[4,2,3,6]]
        expected_result = [3,4,5,1,6,3,2,4]
        self.assertEqual(route(our_list), expected_result)

    def test_one_stowb(self):
        our_list = [[3],[4],[1],[5],[2],[6]]
        expected_result = [3,4,1,5,2,6]
        self.assertEqual(route(our_list), expected_result)

      

if __name__ == '__main__':
    unittest.main()
