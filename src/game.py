import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame


import numpy as np
import random
from pygame.locals import *


def main():
    # Initialize Pygame
    pygame.init()

    # Constants
    GRID_SIZE = (10, 10)
    CELL_SIZE = 50
    WINDOW_SIZE = (GRID_SIZE[1] * CELL_SIZE, GRID_SIZE[0] * CELL_SIZE)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GRAY = (200, 200, 200)

    # Game variables
    num_ants = 5
    pheromone_decay = 0.9
    pheromone_boost = 10
    pheromone_initial = 1

    # Create window
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Pheromone Frenzy")

    # Initialize grid with obstacles and food
    grid = np.zeros(GRID_SIZE)
    food_positions = [(random.randint(0, GRID_SIZE[0]-1), random.randint(0, GRID_SIZE[1]-1)) for _ in range(5)]
    obstacles = [(random.randint(0, GRID_SIZE[0]-1), random.randint(0, GRID_SIZE[1]-1)) for _ in range(10)]
    for food in food_positions:
        grid[food] = 2  # Food
    for obstacle in obstacles:
        grid[obstacle] = 3  # Obstacle

    # Initialize pheromone grid
    pheromones = np.full(GRID_SIZE, pheromone_initial, dtype=float)

    # Ant class
    class Ant:
        def __init__(self, start_pos):
            self.pos = start_pos
            self.path = [start_pos]  # Track the ant's path
            self.has_food = False
        
        def move(self, grid, pheromones):
            # Define possible moves
            possible_moves = [(self.pos[0] + dx, self.pos[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            possible_moves = [move for move in possible_moves if 0 <= move[0] < GRID_SIZE[0] and 0 <= move[1] < GRID_SIZE[1]]
            
            # Filter out obstacles
            possible_moves = [move for move in possible_moves if grid[move] != 3]
            
            # Select next move based on pheromone strength
            if possible_moves:
                pheromone_levels = [pheromones[move] for move in possible_moves]
                total_pheromone = sum(pheromone_levels)
                probabilities = [p / total_pheromone for p in pheromone_levels]
                next_move = random.choices(possible_moves, weights=probabilities, k=1)[0]
                self.pos = next_move
                self.path.append(next_move)

    # Initialize ants
    ants = [Ant((0, 0)) for _ in range(num_ants)]

    # Game loop
    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(WHITE)
        
        # Draw grid
        for row in range(GRID_SIZE[0]):
            for col in range(GRID_SIZE[1]):
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if grid[row, col] == 3:  # Obstacle
                    pygame.draw.rect(screen, BLACK, cell_rect)
                elif grid[row, col] == 2:  # Food
                    pygame.draw.rect(screen, GREEN, cell_rect)
                elif pheromones[row, col] > pheromone_initial:  # Pheromone trail
                    color_intensity = min(255, int(pheromones[row, col] * 10))
                    pygame.draw.rect(screen, (color_intensity, color_intensity, 255), cell_rect)
                pygame.draw.rect(screen, GRAY, cell_rect, 1)
        
        # Move ants and update pheromones
        for ant in ants:
            ant.move(grid, pheromones)
            pheromones[ant.pos] += pheromone_boost  # Reinforce path
            
            # Check for food
            if grid[ant.pos] == 2:
                grid[ant.pos] = 0  # Remove food after collection
                ant.has_food = True
                # Bring ant back to colony or reset

            # Draw ant
            ant_rect = pygame.Rect(ant.pos[1] * CELL_SIZE, ant.pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.circle(screen, RED if ant.has_food else BLUE, ant_rect.center, CELL_SIZE // 4)
        
        # Evaporate pheromones
        pheromones *= pheromone_decay

        pygame.display.flip()
        clock.tick(5)  # Adjust speed for testing
        
        # Handle exit
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

    pygame.quit()
if __name__ == "__main__":
    main()