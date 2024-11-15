import sys
import os

import unittest
from pathlib import Path

# Додаємо абсолютний шлях до каталогу 'src'
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))
from list_based_priority_queue import PriorityQueue

class TestListBasedPriorityQueue(unittest.TestCase):
    def test1(self): # Тест перевіряє, чи черга зберігає елементи у правильному порядку після їх вставки з різними пріоритетами
        queue = PriorityQueue()
        queue.insert("low_priority", 1)
        queue.insert("medium_priority", 5)
        queue.insert("high_priority", 10)
        self.assertEqual(str(queue), "(Value: high_priority, Priority: 10) -> (Value: medium_priority, Priority: 5) -> (Value: low_priority, Priority: 1)")

    def test2(self): # Тест перевіряє, чи метод peek повертає елемент з найвищим пріоритетом без видалення його з черги
        queue = PriorityQueue()
        queue.insert("low_priority", 1)
        queue.insert("medium_priority", 5)
        queue.insert("high_priority", 10)
        self.assertEqual(queue.peek(), "high_priority")

    def test3(self): # Тест перевіряє, чи метод pop видаляє і повертає елемент з найвищим пріоритетом
        queue = PriorityQueue()
        queue.insert("low_priority", 1)
        queue.insert("medium_priority", 5)
        queue.insert("high_priority", 10)
        self.assertEqual(queue.pop(), "high_priority")
        self.assertEqual(str(queue), "(Value: medium_priority, Priority: 5) -> (Value: low_priority, Priority: 1)")

    def test4(self): # Тест перевіряє, чи черга стає порожньою після видалення всіх елементів
        queue = PriorityQueue()
        queue.insert("low_priority", 1)
        queue.insert("medium_priority", 5)
        queue.insert("high_priority", 10)
        queue.pop()
        queue.pop()
        queue.pop()
        self.assertTrue(queue.is_empty())

    def test5(self): # Тест перевіряє, чи новостворена черга є порожньою
        queue = PriorityQueue()
        self.assertTrue(queue.is_empty())

    def test6(self): # Тест перевіряє, чи черга знову стає порожньою після вставки і видалення одного елемента
        queue = PriorityQueue()
        queue.insert("item", 1)
        queue.pop()
        self.assertTrue(queue.is_empty())

    def test_pop_empty_queue_returns_none(self):
        """Перевіряє, чи pop на порожній черзі повертає None, хоча це "неправильний" результат для звичайного pop."""
        queue = PriorityQueue()
        result = queue.pop()
        # Тут ми очікуємо, що результат буде None, і тест вважається успішним, якщо так і є.
        self.assertIsNone(result, "Очікуємо None при спробі pop на порожній черзі")

if __name__ == '__main__':
    unittest.main()