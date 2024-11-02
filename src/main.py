import pygame
import random
from ant import Ant
import os
#os.environ["SDL_VIDEODRIVER"] = "dummy"

# Initialize Pygame
pygame.init()


# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FOOD_COLOR = (255, 223, 0)
ANT_COLOR = (0, 0, 0)
PHEROMONE_COLOR = (173, 216, 230)
OBSTACLE_COLOR = (128, 128, 128)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pheromone Frenzy")

# Grid Setup
grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
food_positions = [(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)) for _ in range(5)]
for x, y in food_positions:
    grid[y][x] = "food"

# Create list of ants
ants = [Ant(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)) for _ in range(5)]

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw food
    for x, y in food_positions:
        pygame.draw.rect(screen, FOOD_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update and draw ants
    for ant in ants:
        ant.move(grid)
        pygame.draw.rect(screen, ANT_COLOR, (ant.x * CELL_SIZE, ant.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Control game speed

pygame.quit()
