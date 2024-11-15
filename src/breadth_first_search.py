from collections import deque
import os


class LabyrinthSolver:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.start = None
        self.destination = None
        self.matrix = []
    
    def read_input(self):
        """Зчитує вхідні дані з файлу з перевіркою на наявність файлу."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Файл '{self.input_file}' не знайдено.")

        with open(self.input_file, 'r', encoding='utf-8') as file:
            self.start = tuple(map(int, file.readline().strip().split(',')))
            self.destination = tuple(map(int, file.readline().strip().split(',')))
            rows, cols = map(int, file.readline().strip().split(','))
            self.matrix = [list(map(int, file.readline().strip().split())) for _ in range(rows)]

        if not self.is_within_bounds(self.start, rows, cols) or not self.is_within_bounds(self.destination, rows, cols):
            raise ValueError("Координати старту або призначення виходять за межі матриці.")

    @staticmethod
    def is_within_bounds(point, rows, cols):
        x, y = point
        return 0 <= x < rows and 0 <= y < cols

    def is_valid(self, x, y, visited):
        rows, cols = len(self.matrix), len(self.matrix[0])
        return 0 <= x < rows and 0 <= y < cols and self.matrix[x][y] == 1 and not visited[x][y]

    def find_shortest_path(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(self.start[0], self.start[1], 0)])
        visited = [[False] * len(self.matrix[0]) for _ in range(len(self.matrix))]
        visited[self.start[0]][self.start[1]] = True

        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == self.destination:
                return dist

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny, visited):
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

        return -1

    def write_output(self, result):
        """Записує результат у файл."""
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(str(result))

    def solve(self):
        """Основний метод для запуску розв'язку лабіринту."""
        self.read_input()
        shortest_path = self.find_shortest_path()
        self.write_output(shortest_path)


if __name__ == "__main__":
    solver = LabyrinthSolver('src/input.txt', 'src/output.txt')
    solver.solve()
