import pygame

pygame.init()

# Game window settings
screenX = 1080
screenY = 720

screen = pygame.display.set_mode((screenX, screenY))

# Window title
pygame.display.set_caption("Josefina's Pong")

# Paddle image
paddleImage = pygame.image.load("images/paleta.png")

class Paleta2(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = paddleImage
        self.rect = self.image.get_rect()
        self.pts = 0

