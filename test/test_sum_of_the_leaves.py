import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest 
from src.the_sum_of_the_leaves import *


class TestTheSumOfTheLeaves(unittest.TestCase):
    def test1(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        self.assertEqual(branchSums(root), 20)


    
if __name__ == '__main__':
    unittest.main()
