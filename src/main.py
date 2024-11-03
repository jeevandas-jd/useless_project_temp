import pygame
import sys
from .game_manager import GameManager

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
FPS = 30

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pheromone Frenzy")
clock = pygame.time.Clock()

# Initialize GameManager
game_manager = GameManager(screen)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Clear screen

        # Update and draw game
        game_manager.update()
        game_manager.draw()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
