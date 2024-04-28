import pygame
import sys


class Game:
    def __init__(self, screen, agent, maze):
        self.screen = screen
        self.agent = agent
        self.maze = maze
        self.running = True
        self.last_move_time = (
            pygame.time.get_ticks()
        )  # Tiempo desde el último movimiento

    def update(self):
        current_time = pygame.time.get_ticks()
        if (
            self.agent.path
            and self.running
            and current_time - self.last_move_time > 1000
        ):  # 1000 milisegundos entre movimientos
            moved = self.agent.move_along_path()
            self.last_move_time = (
                current_time  # Restablecer el tiempo del último movimiento
            )

            if not moved or self.agent.position == self.agent.goal:
                self.running = False

    def draw(self):
        self.screen.fill((255, 255, 255))  # Limpiar pantalla con fondo blanco
        self.maze.draw(self.screen)  # Dibujar el laberinto
        self.agent.draw(self.screen)  # Dibujar el agente
        pygame.display.flip()  # Actualizar la pantalla

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def print_result(self):
        # Imprimir el resultado del juego una vez que termina
        if self.agent.path is not None:
            print(f"Number of movements required: {len(self.agent.path) + 1}")
        else:
            print("No solution")

    def is_running(self):
        return self.running

    def run(self):
        # Bucle principal del juego
        clock = pygame.time.Clock()
        while self.is_running():
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)  # Mantener el juego corriendo a 60 FPS

        # Llamar a print_result para mostrar los resultados después de terminar el juego
        self.print_result()
