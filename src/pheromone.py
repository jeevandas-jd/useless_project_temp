
from game_manager import GRID_SIZE,GRID_HEIGHT,GRID_WIDTH

class PheromoneTrail:
    def __init__(self):
        self.pheromone_map = {}

    def add_pheromone(self, x, y):
        if (x, y) in self.pheromone_map:
            self.pheromone_map[(x, y)] = min(self.pheromone_map[(x, y)] + 0.1, 1.0)
        else:
            self.pheromone_map[(x, y)] = 1.0

    def update(self):
        # Decay pheromones over time
        to_remove = []
        for position, strength in self.pheromone_map.items():
            new_strength = strength - 0.01
            if new_strength <= 0:
                to_remove.append(position)
            else:
                self.pheromone_map[position] = new_strength

        for position in to_remove:
            del self.pheromone_map[position]

    def draw(self, screen, pheromone_image):
        for (x, y), strength in self.pheromone_map.items():
            if strength > 0:
                screen.blit(pheromone_image, (x * GRID_SIZE, y * GRID_SIZE))
