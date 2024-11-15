import sys
import os

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None
        self.prev = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.head:
            # Порожня черга, встановлюємо голову і хвіст на новий елемент
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            # Знаходимо позицію для вставки з урахуванням пріоритету
            while current and current.priority >= priority:
                current = current.next
            
            if not current:
                # Додаємо новий вузол в кінець
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            elif current == self.head:
                # Вставка на початок
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                # Вставка в середину черги
                previous_node = current.prev
                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current
                current.prev = new_node

    def pop(self):
        if not self.head:
            return None
        # Вилучення першого елемента (з найвищим пріоритетом)
        highest_priority_node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return highest_priority_node.value

    def peek(self):
        # Повертає значення елемента з найвищим пріоритетом без його видалення
        return self.head.value if self.head else None

    def is_empty(self):
        return self.head is None

    def __str__(self):
        # Для перегляду черги без її зміни
        elements = []
        current = self.head
        while current:
            elements.append(f"(Value: {current.value}, Priority: {current.priority})")
            current = current.next
        return " -> ".join(elements)
