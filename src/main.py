import pygame
import os
import sys
from parseador import parse_input
from game import Game
from agent import Agent
from maze import Maze

# Configuraciones iniciales del juego
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
FPS = 60


def main():
    # Inicializar Pygame y configurar la ventana
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Laberinto Saltarín")

    # Ruta absoluta al directorio actual de main.py
    current_path = os.path.dirname(os.path.abspath(__file__))
    # Ruta absoluta al archivo entrada.txt
    file_path = os.path.join(current_path, "../data/entrada3.txt")
    # Cargar el laberinto desde el archivo de entrada
    mazes = parse_input(file_path)

    # Asumiendo que `parse_input` devuelve una lista con al menos un laberinto
    for maze_data in mazes:
        maze = Maze(maze_data)
        agent = Agent(maze)

        # Puedes cambiar 'uniform_cost' por 'dfs' para utilizar DFS
        agent.search_path(method="uniform_cost")

        # Inicializar el juego con las instancias de screen, agent y maze
        game = Game(screen, agent, maze)

        # Bucle principal del juego
        clock = pygame.time.Clock()
        while game.is_running() and agent.path is not None:
            game.handle_events()
            if game.is_running():
                game.update()
            game.draw()
            clock.tick(FPS)

    # Espera activa hasta que el usuario cierre la ventana
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
