# agent.py

from search_methods import dfs, uniform_cost_search
import pygame


class Agent:
    def __init__(self, start_position, goal_position, cell_size=80):
        self.position = start_position
        self.goal = goal_position
        self.path = None
        self.cell_size = cell_size

    def search_path(self, grid, method="dfs"):
        if method == "dfs":
            self.path = dfs(grid, self.position, self.goal)
            print("Goal Position:", self.goal)
        elif method == "uniform_cost":
            self.path = uniform_cost_search(grid, self.position, self.goal)
        else:
            raise ValueError(f"Unknown search method: {method}")
        return self.path

    def move_along_path(self):
        if self.path:
            # print("Current position:", self.position)
            # print("Next move:", self.path[0])
            self.position = self.path.pop(0)
            # print("Moved to:", self.position)
            return True
        else:
            print("No more moves left or no path")
        return False

    def draw(self, screen):
        screen_position = (
            self.position[0] * self.cell_size + self.cell_size // 2,
            self.position[1] * self.cell_size + self.cell_size // 2,
        )
        pygame.draw.circle(
            screen, (0, 0, 255), screen_position, self.cell_size // 3, width=3
        )
