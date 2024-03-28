class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class Queue:
    def __init__(self):
        self.queue = []

    def swap_elements(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def add(self, value, priority):
        new_node = Node(value, priority)
        self.queue.append(new_node)
        if len(self.queue) > 1:
            for i in range((len(self.queue) - 2) // 2, -1, -1):
                self.heapify(self.queue, i, len(self.queue))

    def heapify(self, arr, node, heap_len):
        left_child = node * 2 + 1
        right_child = node * 2 + 2

        if left_child < heap_len:
            if arr[left_child].priority > arr[node].priority:
                self.swap_elements(arr, left_child, node)
                self.heapify(arr, left_child, heap_len)
        if right_child < heap_len:
            if arr[right_child].priority > arr[node].priority:
                self.swap_elements(arr, right_child, node)
                self.heapify(arr, right_child, heap_len)

    def delete(self):
        if len(self.queue) == 0:
            return None
        if len(self.queue) == 1:
            return self.queue.pop().priority  # Повертаємо пріоритет видаленого елемента
        else:
            max_value = self.queue[0]
            self.queue[0] = self.queue.pop()
            self.heapify(self.queue, 0, len(self.queue))  # Переконуємося, що купа є купою
            return max_value.priority

    def print_queue(self):
        for i in self.queue:
            print("Next task priority:", i.priority)

# Вхідні дані
queue = Queue()
queue.add("Task 1", 3)
queue.add("Task 2", 1)
queue.add("Task 3", 2)

# Вивід черги
queue.print_queue()
