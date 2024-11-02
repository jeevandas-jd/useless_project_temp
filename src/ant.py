import random

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, grid):
        # Check neighboring cells for food or pheromones
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # up, down, left, right
        random.shuffle(directions)  # Randomize direction choice

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if grid[ny][nx] == "food":
                    self.x, self.y = nx, ny  # Move toward food
                    grid[ny][nx] = None  # Collect food
                    return

        # If no food, move randomly
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

        # Keep ants within bounds
        self.x = max(0, min(self.x, len(grid[0]) - 1))
        self.y = max(0, min(self.y, len(grid) - 1))
    
