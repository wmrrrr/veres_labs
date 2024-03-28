import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import unittest
from src.heap_based_priority_queue import *


class TestHeapQueue(unittest.TestCase):
    def test_add(self):
        heap = Queue()
        heap.add("Task 1", 3)
        heap.add("Task 2", 1)
        heap.add("Task 3", 2)

        self.assertEqual(heap.queue[0].priority, 3)

    def test_pop_element(self):
        heap = Queue()
        heap.add("Task 1", 5)
        heap.add("Task 2", 9)
        heap.add("Task 3", 10)
        heap.add("Task 4", 4)
        heap.add("Task 5", 4)
        heap.add("Task 6", 4)
        heap.add("Task 7", 4)

        self.assertEqual(heap.delete(), 10)

    def test_print_empty_queue(self):
        heap = Queue()
        heap.print_queue()
        self.assertEqual(heap.print_queue(), None)


if __name__ == '__main__':
    unittest.main()
