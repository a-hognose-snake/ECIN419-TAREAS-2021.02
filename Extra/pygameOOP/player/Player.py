import pygame

class Player(object):
    # Constructor
    def __init__(self, x, y, width, height):
        # Attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.left = False
        self.right = False
        self.didJump = False
        self.countJumps = 10
        self.countSteps = 0
        self.standing = True
        self.hitbox = (self.x + 2, self.y + 2, self.width - 5, self.height - 2)
        self.health = 10
        self.visible = True

    # Methods
    def draw(self, screen, walkLeft, walkRight, front):
        if self.visible:
            if self.countSteps + 1 >= 60:
                self.countSteps = 0
            if not self.standing:
                if self.left:
                    # [self.countSteps//3]
                    screen.blit((walkLeft[0]), (self.x, self.y))
                    self.countSteps += 1
                elif self.right:
                    screen.blit((walkRight[0]), (self.x, self.y))
                    self.countSteps += 1
                else:
                    # screen.blit(front, (self.x, self.y))
                    if self.right:
                        screen.blit(walkRight[0], (self.x, self.y))
                    else:
                        screen.blit(walkLeft[0], (self.x, self.y))
            else:
                screen.blit(front, (self.x, self.y))
            # view the box
            # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
            pygame.draw.rect(screen, (255, 0, 0), (self.x - 10, self.y - 10, 50, 10))
            pygame.draw.rect(screen, (0, 255, 0), [self.x - 10, self.y - 10, (50 - (50 / 10) * (10 - self.health)), 10])
            self.hitbox = (self.x + 2, self.y + 2, self.width - 5, self.height - 3)
        else:
            self.hitbox = (0, 0, 0, 0)

    def hit(self, screen):
        self.x = 0
        self.y = 410
        self.countSteps = 0
        if self.health > 0:
            self.health -= 2
            fontCollision = pygame.font.Font("resources/fonts/minimal/Minimal3x5.ttf", 25)
            text = fontCollision.render("COLLISION  DETECTED: -2 PTS", True, (255, 255, 255))
            screen.blit(text, (20, 20))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()
        else:
            self.visible = False
            fontCollision = pygame.font.Font("resources/fonts/minimal/Minimal3x5.ttf", 80)
            text = fontCollision.render("Game Over. Press [A]", True, (255, 255, 255))
            screen.blit(text, (20, 20))
