import pygame

from enemy.Enemy import Enemy
from player.Player import Player
from projectile.Projectile import Projectile

# initialize screen
pygame.init()
screenWidth = 1080
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Gatito CyberPunk")

# resources
# background image
image1 = pygame.image.load("resources/images/backgrounds/night_bg.png")
bg = pygame.transform.scale(image1, (1080, 720))
# player's images: cat
sizePlayer = 43
image2 = pygame.image.load("resources/images/cat/Blue_Cat_STAY.png")
front = pygame.transform.scale(image2, (sizePlayer, sizePlayer))
image4 = pygame.image.load("resources/images/cat/Blue_Cat_R1.png")
walkRight = [pygame.transform.scale(image4, (sizePlayer, sizePlayer))]
image3 = pygame.image.load("resources/images/cat/Blue_Cat_L1.png")
walkLeft = [pygame.transform.scale(image3, (sizePlayer, sizePlayer))]

# main loop variables
clock = pygame.time.Clock()
# sounds
fireSound = pygame.mixer.Sound("resources/sounds/laserGun.mp3")
hitSound = pygame.mixer.Sound("resources/sounds/waterImpact.mp3")
pygame.mixer.music.load("resources/sounds/Kesha- your love is my drug 8-bit S L O W E D.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
jumpSound = pygame.mixer.Sound("resources/sounds/Shoot.wav")
# fonts
font = pygame.font.Font("resources/fonts/minimal/Minimal3x5.ttf", 25)
# others
score = 0
left = False
right = False
run = True
bullets = []
shootingLoop = 0
# instance of Player
cat = Player(0, 410, sizePlayer, sizePlayer)
# instance of Enemy
slime = Enemy(100, 405, sizePlayer, sizePlayer, 600)


# draw on game screen
def reDrawScreen():
    screen.blit(bg, (0, 0))
    text = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(text, (975, 690))
    # draw player: cat
    cat.draw(screen, walkLeft, walkRight, front)
    for b in bullets:
        # draw bullet
        b.draw(screen)
    # draw enemy: slime
    slime.draw(screen)

    pygame.display.update()


# main loop
while run:
    # 30 frames per second
    clock.tick(50)
    # makes shooting smoother
    if shootingLoop > 0:
        shootingLoop += 1
    if shootingLoop > 3:
        shootingLoop = 0

    # ends the game when you close the game screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # player and enemy collision
    if cat.hitbox[1] < slime.hitbox[1] + slime.hitbox[3] and cat.hitbox[1] + cat.hitbox[3] > slime.hitbox[1]:
        if cat.hitbox[0] + cat.hitbox[2] > slime.hitbox[0] and cat.hitbox[0] < slime.hitbox[0] + slime.hitbox[2]:
            cat.hit(screen)
            hitSound.play()
            score -= 2
    # player's projectile collision with enemy
    for bullet in bullets:
        # bullet hits the enemy
        if bullet.y - bullet.radius < slime.hitbox[1] + slime.hitbox[3] and bullet.y + bullet.radius > slime.hitbox[1]:
            if bullet.x + bullet.radius > slime.hitbox[0] and bullet.x - bullet.radius < slime.hitbox[0] + slime.hitbox[2]:
                slime.hit()
                score += 3
                bullets.pop(bullets.index(bullet))
                hitSound.play()
        if screenWidth > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            # deletes the bullet from the list if its not on the screen's range
            bullets.pop(bullets.index(bullet))
    # keyboard keys actions
    # move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_k] and shootingLoop == 0:
        # shoot weapon
        fireSound.play()
        if cat.left:
            # facing refers to the direction in which the cat was moving before shooting
            facing = -1
        else:
            facing = 1
        # projectiles
        if len(bullets) < 5:
            bullets.append(Projectile((round(cat.x + cat.width // 2)) + 2, (round(cat.y + cat.height // 2)) - 4, 3, (255, 255, 255), facing))
        shootingLoop = 1
    if keys[pygame.K_LEFT] and cat.x > cat.velocity:
        # move left
        cat.x -= cat.velocity
        cat.left = True
        cat.right = False
        cat.standing = False
    elif keys[pygame.K_RIGHT] and cat.x < screenWidth - cat.width - cat.velocity:
        # move right
        cat.x += cat.velocity
        cat.left = False
        cat.right = True
        cat.standing = False
    else:
        # standing still
        # left = False
        # right = False
        cat.standing = True
        cat.countSteps = 0
        # fly REMOVE? Make animation
        if keys[pygame.K_UP] and cat.y > cat.velocity:
            # move up
            cat.y -= cat.velocity
        if keys[pygame.K_DOWN] and cat.y < screenHeight - cat.height - cat.velocity:
            # move down
            cat.y += cat.velocity
        # REMOVE?
    if not cat.didJump:
        # not jumping
        if keys[pygame.K_SPACE]:
            # jump
            jumpSound.play()
            cat.didJump = True
            cat.left = False
            cat.right = False
            cat.countSteps = 0
        #
        if keys[pygame.K_UP] and cat.y > cat.velocity:
            # move up
            cat.y -= cat.velocity
        if keys[pygame.K_DOWN] and cat.y < screenHeight - cat.height - cat.velocity:
            # move down
            cat.y += cat.velocity
    else:
        # jump
        if cat.countJumps >= -10:
            neg = 1
            if cat.countJumps < 0:
                neg = -1
            # moves up and down when character jumps (uses a quadratic function)
            cat.y -= (cat.countJumps ** 2) * 0.5 * neg
            cat.countJumps -= 1
        else:
            cat.didJump = False
            cat.countJumps = 10
    reDrawScreen()

pygame.quit()
