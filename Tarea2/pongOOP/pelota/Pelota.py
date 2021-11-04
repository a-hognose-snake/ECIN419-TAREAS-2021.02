import pygame

pygame.init()

# Game window settings
screenX = 1080
screenY = 720

screen = pygame.display.set_mode((screenX, screenY))

# Window title
pygame.display.set_caption("Josefina's Pong")

# Ball image
ballImage = pygame.image.load("images/bola.png")

class Pelota(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ballImage
        self.rect = self.image.get_rect()
        self.speed = 9.8
        self.cambio_x = 1
        self.cambio_y = 1
