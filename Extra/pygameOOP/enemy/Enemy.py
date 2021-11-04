import pygame

class Enemy(object):
    # enemy's images:
    # front = pygame.transform.scale(pygame.image.load("resources/images/slime/Slime.png"), (88, 88))
    size = 43
    walkRight = [pygame.transform.scale(pygame.image.load("resources/images/slime/Slime_R1.png"), (size, size)),
                 pygame.transform.scale(pygame.image.load("resources/images/slime/Slime_R2.png"), (size, size)),
                 pygame.transform.scale(pygame.image.load("resources/images/slime/Slime_R3.png"), (size, size)),
                 pygame.transform.scale(pygame.image.load("resources/images/slime/Slime_R4.png"), (size, size))]
    walkLeft = [pygame.transform.scale(pygame.image.load("resources/images/slime/Slime_L1.png"), (size, size)),
                pygame.transform.scale(pygame.image.load("resources/images/slime/Slime_L2.png"), (size, size)),
                pygame.transform.scale(pygame.image.load("resources/images/slime/Slime_L3.png"), (size, size)),
                pygame.transform.scale(pygame.image.load("resources/images/slime/Slime_L4.png"), (size, size))]

    # Constructor
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.countSteps = 0
        self.velocity = 3
        self.hitbox = (self.x + 8, self.y + 10, self.width - 15, self.height - 20)
        self.health = 10
        self.visible = True

    # Methods
    def draw(self, screen):
        self.move()
        if self.visible:
            # will show each image for 3 frames. 3 x 4
            if self.countSteps + 1 >= (3 * 4):
                self.countSteps = 0
            if self.velocity > 0:
                # draw walkRight images
                screen.blit(self.walkRight[self.countSteps // 3], (self.x, self.y))
                self.countSteps += 1
            else:
                # draw walkLeft images
                screen.blit(self.walkLeft[self.countSteps // 3], (self.x, self.y))
                self.countSteps += 1

            pygame.draw.rect(screen, (255, 0, 0), (self.x - 3, self.y, 50, 10))
            pygame.draw.rect(screen, (0, 255, 0), [self.x - 3, self.y, (50 - (50 / 10) * (10 - self.health)), 10])
            # view the box
            # pygame.draw.rect(screen, (255, 0, 0), self.hit box, 2)
            self.hitbox = (self.x + 8, self.y + 10, self.width - 15, self.height - 20)
        else:
            self.hitbox = (0, 0, 0, 0)

    def move(self):
        if self.velocity > 0:
            # if we are moving right
            if self.x < self.path[1] + self.velocity:
                # if we are not at the end of the path, keep moving
                self.x += self.velocity
            else:
                # else, change direction and move back the other way
                self.velocity = self.velocity * -1
                self.x += self.velocity
                self.countSteps = 0
        else:
            # if we are moving left
            if self.x > self.path[0] - self.velocity:
                # if we are not at the end of the path, keep moving
                self.x += self.velocity
            else:  # else, change direction
                self.velocity = self.velocity * -1
                self.x += self.velocity
                self.countSteps = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
