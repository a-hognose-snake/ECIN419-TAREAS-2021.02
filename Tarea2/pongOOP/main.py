import pygame

# Classes
from paleta1.Paleta1 import Paleta1
from paleta2.Paleta2 import Paleta2
from pelota.Pelota import Pelota

# Initialize
pygame.init()

# Game window settings
screenX = 1080
screenY = 720

screen = pygame.display.set_mode((screenX, screenY))

# Window title
pygame.display.set_caption("Josefina's Pong")

# Background image
bgImage = pygame.image.load("images/fondo.jpg").convert()
bg = pygame.transform.scale(bgImage, (screenX, screenY))

# Instances of the class - Sprites
paleta1 = Paleta1()
paleta1.rect.x = screenX * 0.04
paleta1.rect.y = screenY * 0.45

paleta2 = Paleta2()
paleta2.rect.x = screenX * 0.95
paleta2.rect.y = screenY * 0.45

paddle_speed = 10

pelota = Pelota()
pelota.rect.x = screenX * 0.489
pelota.rect.y = screenY * 0.5

# Group all the sprites so they can only interact between them
all_sprites = pygame.sprite.Group()
all_sprites.add(paleta1, paleta2, pelota)

# Update and draw function
def updateDraw():
    # Draws background image
    screen.blit(bg, (0, 0))

    # Updates all Sprites
    all_sprites.draw(screen)

    # Updates game screen
    pygame.display.update()


# Game variables
run = True

clock_tick_rate = 20
clock = pygame.time.Clock()

# Main loop
while run:

    clock.tick(clock_tick_rate)

    # Events
    for event in pygame.event.get():

        # Quit
        if event.type == pygame.QUIT:
            run = False

    # Move paletas
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paleta1.rect.y += -paddle_speed
    if key[pygame.K_s]:
        paleta1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paleta2.rect.y += -paddle_speed
    if key[pygame.K_DOWN]:
        paleta2.rect.y += paddle_speed

    # Pelota Bouncing Movement Formula ############
    pelota.rect.x += pelota.speed * pelota.cambio_x
    pelota.rect.y += pelota.speed * pelota.cambio_y
    ###############################################

    # Limits
    if pelota.rect.y > screenY - 10:
        print("pelota tocó limite superior")
        pelota.cambio_y = -1

    if pelota.rect.y < 1:
        print("pelota tocó limite inferior")
        pelota.cambio_y = 1

    # Points
    if pelota.rect.x > screenX - 10:
        print("")
        print("PUNTO PARA PALETA 1")
        print("")
        print("pelota tocó limite derecho")
        pelota.rect.x, pelota.rect.y = (screenX * 0.489), (screenY * 0.5)
        pelota.cambio_x = -1
        paleta1.pts += 1
        paleta2.pts -= 0.5

    if pelota.rect.x < 1:
        print("")
        print("PUNTO PARA PALETA 2")
        print("")
        print("pelota tocó limite izquierdo")
        pelota.rect.x, pelota.rect.y = (screenX * 0.489), (screenY * 0.5)
        pelota.cambio_x = 1
        paleta1.pts -= 0.5
        paleta2.pts += 1

    # Collisions
    if paleta1.rect.colliderect(pelota.rect):
        pelota.cambio_x = 1
    if paleta2.rect.colliderect(pelota.rect):
        pelota.cambio_x = -1

    # Update screen
    updateDraw()

# Show winner
print("")
print("##########################################")
if int(paleta1.pts) < int(paleta2.pts):
    print("GANADOR: PALETA 2")

elif int(paleta1.pts) > int(paleta2.pts):
    print("GANADOR: PALETA 1")

else:
    print("No hay ganador.")
print("##########################################")
print("")
print("Paleta 1: " + str(paleta1.pts) + " puntos")
print("Paleta 2: " + str(paleta2.pts) + " puntos")

# Game over
pygame.quit()
