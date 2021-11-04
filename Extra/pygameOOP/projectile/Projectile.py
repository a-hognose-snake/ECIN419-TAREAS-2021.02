import pygame
class Projectile(object):
    # Constructor
    def __init__(self, x, y, radius, color, facing):
        # Attributes
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 29 * facing

    # Methods
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
