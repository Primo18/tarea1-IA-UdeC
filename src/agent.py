import pygame
import heapq


class Agent:
    def __init__(self, maze, cell_size=80):
        self.maze = maze
        self.position = maze.start
        self.goal = maze.goal
        self.path = None
        self.cell_size = cell_size

    def dfs(self):
        stack = [(self.position, [self.position])]
        visited = set()
        visited.add(self.position)  # Añadir la posición inicial a visitados

        while stack:
            current_position, path = stack.pop()
            if current_position == self.goal:
                self.path = path
                return path

            neighbors = self.maze.find_neighbors(current_position)
            for new_position in neighbors:
                if new_position not in visited:
                    visited.add(new_position)
                    stack.append((new_position, path + [new_position]))

        print("No se encontró solución")
        return None

    def search_path(self, method="dfs"):
        if method == "dfs":
            result = self.dfs()
        elif method == "uniform_cost":
            result = self.uniform_cost_search()
        else:
            raise ValueError(f"Método de búsqueda desconocido: {method}")

        if result:
            print(f"Meta alcanzada en {len(result) - 1} movimientos")
            return result
        else:
            print("No se encontró solución")
            return None

    def uniform_cost_search(self):
        queue = [(0, self.position, [self.position])]
        visited = set()
        visited.add(self.position)  # Añadir la posición inicial a visitados
        while queue:
            cost, current_position, path = heapq.heappop(queue)

            if current_position == self.goal:
                self.path = path
                return path

            neighbors = self.maze.find_neighbors(current_position)
            for new_position in neighbors:
                if new_position not in visited:
                    visited.add(new_position)
                    new_cost = cost + 1  # Costo uniforme de cada paso
                    heapq.heappush(
                        queue, (new_cost, new_position, path + [new_position])
                    )
        return None

    def move_along_path(self):
        if self.path:
            next_position = self.path.pop(0)
            if self.maze.is_valid_move(next_position):
                self.position = next_position
                return True
            else:
                print("Movimiento inválido")
                return False

    def draw(self, screen):
        screen_position = (
            self.position[1] * self.cell_size + self.cell_size // 2,
            self.position[0] * self.cell_size + self.cell_size // 2,
        )
        pygame.draw.circle(
            screen, (0, 0, 255), screen_position, self.cell_size // 3, width=3
        )
