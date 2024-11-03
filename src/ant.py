
import random

from .game_manager import GRID_SIZE,GRID_HEIGHT,GRID_WIDTH

class Ant:
    def __init__(self, image, game_manager):
        self.image = image
        self.game_manager = game_manager
        self.position = [10, 10]  # Start at the colony
        self.speed = 1

    def update(self):
        # Basic random movement logic
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        new_x = self.position[0] + dx
        new_y = self.position[1] + dy

        # Check if movement is valid
        if self.is_valid_move(new_x, new_y):
            self.position = [new_x, new_y]
            self.game_manager.pheromone_trail.add_pheromone(new_x, new_y)

    def is_valid_move(self, x, y):
        return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT and self.game_manager.grid[y][x] != 'obstacle'

    def draw(self, screen):
        screen.blit(self.image, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE))
