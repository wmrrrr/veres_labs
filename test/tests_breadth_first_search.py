import sys
import os

import unittest
import sys
from pathlib import Path

# Додаємо абсолютний шлях до каталогу 'src'
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))

from breadth_first_search import LabyrinthSolver  # або імпортуйте інші модулі, як потрібно


class TestBreadthFirstSearch(unittest.TestCase):
    
    def setUp(self):
        # Налаштовуємо вхідні та вихідні файли для тестування
        self.solver = LabyrinthSolver('src/test_input.txt', 'src/test_output.txt')
    
    def test_read_input(self):
        # Створюємо тестові вхідні дані
        with open('src/test_input.txt', 'w') as f:
            f.write("0,0\n7,5\n10,10\n")
            f.write("1 1 1 1 1 0 0 1 1 1\n0 1 1 1 1 1 0 1 0 1\n")
            f.write("0 0 1 0 1 1 1 0 0 1\n1 0 1 1 1 0 1 1 0 1\n")
            f.write("0 0 0 1 0 0 0 1 0 1\n1 0 1 1 1 0 0 1 1 0\n")
            f.write("0 0 0 0 1 0 0 1 0 1\n0 1 1 1 1 1 1 1 0 0\n")
            f.write("1 1 1 1 1 0 0 1 1 1\n0 0 1 0 0 1 1 0 0 1\n")
        
        self.solver.read_input()
        
        # Перевіряємо, чи правильно зчитано вхідні дані
        self.assertEqual(self.solver.start, (0, 0))
        self.assertEqual(self.solver.destination, (7, 5))
        self.assertEqual(len(self.solver.matrix), 10)
        self.assertEqual(len(self.solver.matrix[0]), 10)
    
    def test_find_shortest_path(self):
        # Використовуємо раніше зчитані дані для перевірки шляху
        self.solver.read_input()
        result = self.solver.find_shortest_path()
        
        # Перевіряємо, чи результат відповідає очікуваному значенню
        self.assertEqual(result, 12)
    
    def test_write_output(self):
        # Записуємо результат і перевіряємо вихідні дані
        self.solver.write_output(12)
        
        with open('src/test_output.txt', 'r') as f:
            result = int(f.read().strip())
        
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()