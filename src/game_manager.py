import pygame
from ant import Ant
from pheromone import PheromoneTrail
from random import randint

GRID_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 20

class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.ants = []
        self.pheromone_trail = PheromoneTrail()

        # Load images
        self.images = {
            'empty': pygame.image.load("images/empty.png"),
            'obstacle': pygame.image.load("images/obstacle.png"),
            'food': pygame.image.load("images/food.png"),
            'hazard': pygame.image.load("images/hazard.png"),
            'colony': pygame.image.load("images/colony.png"),
            'ant': pygame.image.load("images/ant.png"),
            'pheromone': pygame.image.load("images/pheromone.png"),
        }

        # Initialize ants
        self.spawn_ants()

        # Place random obstacles, food, and hazards
        self.setup_grid()

    def spawn_ants(self):
        for _ in range(10):  # Number of ants
            ant = Ant(self.images['ant'], self)
            self.ants.append(ant)

    def setup_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if randint(0, 10) > 8:  # Randomly place obstacles and food
                    self.grid[y][x] = 'obstacle' if randint(0, 1) == 0 else 'food'

    def update(self):
        # Update ants and pheromone trails
        for ant in self.ants:
            ant.update()

        self.pheromone_trail.update()

    def draw(self):
        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                cell_type = self.grid[y][x] or 'empty'
                self.screen.blit(self.images[cell_type], (x * GRID_SIZE, y * GRID_SIZE))

        # Draw pheromones
        self.pheromone_trail.draw(self.screen, self.images['pheromone'])

        # Draw ants
        for ant in self.ants:
            ant.draw(self.screen)
