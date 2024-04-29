# maze.py
import pygame


class Maze:
    def __init__(self, maze_config):
        self.rows, self.cols, start_y, start_x, end_y, end_x, self.grid = maze_config
        self.start = (start_y, start_x)
        self.goal = (end_y, end_x)
        self.cell_size = 80
        self.wall_color = (0, 0, 0)

    def draw(self, screen):
        for y in range(self.rows):
            for x in range(self.cols):
                cell_value = self.grid[y][x]
                screen_x = x * self.cell_size
                screen_y = y * self.cell_size
                pygame.draw.rect(
                    screen,
                    self.wall_color,
                    (screen_x, screen_y, self.cell_size, self.cell_size),
                    1,
                )
                font = pygame.font.Font(None, 36)
                text = font.render(str(cell_value), True, self.wall_color)
                text_rect = text.get_rect(
                    center=(
                        screen_x + self.cell_size // 2,
                        screen_y + self.cell_size // 2,
                    )
                )
                screen.blit(text, text_rect)
                if (y, x) == self.start:
                    pygame.draw.circle(
                        screen,
                        (0, 255, 0),
                        text_rect.center,
                        self.cell_size // 3,
                        width=3,
                    )
                elif (y, x) == self.goal:
                    pygame.draw.circle(
                        screen,
                        (255, 0, 0),
                        text_rect.center,
                        self.cell_size // 3,
                        width=3,
                    )

    def get_cell_value(self, position):
        y, x = position
        return self.grid[y][x]

    def is_valid_move(self, position):
        y, x = position
        if 0 <= x < self.cols and 0 <= y < self.rows:
            # Permitir moverse a la celda si es la meta, incluso si su valor es cero.
            return self.grid[y][x] != 0 or (y, x) == self.goal
        return False

    # Implementa el método `find_neighbors` que recibe una posición `(y, x)` y retorna una lista con las posiciones vecinas válidas a las que se puede mover el agente.
    def find_neighbors(self, position):
        y, x = position
        jump_value = self.get_cell_value((y, x))
        potential_moves = [
            (y, x + jump_value),
            (y, x - jump_value),
            (y + jump_value, x),
            (y - jump_value, x),
        ]
        neighbors = []
        for new_y, new_x in potential_moves:
            if (
                0 <= new_x < self.cols
                and 0 <= new_y < self.rows
                and self.is_valid_move((new_y, new_x))
            ):
                neighbors.append((new_y, new_x))
        return neighbors
