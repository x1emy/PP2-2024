import random
import time
import sys
import pygame

pygame.init()

fps = 60
time1 = pygame.time.Clock()
font = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))
bg = pygame.image.load("img/road.png")
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SPEED = 1
SCORE = 0
SCORE2 = -1
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill((255, 255, 255))
pygame.display.set_caption("Race")

#ENEMY
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/enemy.png")
        
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 3, self.image.get_height() // 3))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    #MOVING ENEMY
    def move(self):
        global SCORE
        self.rect.move_ip(0, 10)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#PLAYER
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/car.png")

        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (160, SCREEN_HEIGHT - 80)
#MOVING PLAYER
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(10, 0)

#COIN
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/coin.png")
        
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#MOVING COIN
    def move(self):
        global SCORE2
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

P1 = Player() #GROUPPING USING SPRITE
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 500)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 50
            new_coin = Coin()
            all_sprites.add(new_coin)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #BACKGROUND AND DISPLAY
    DISPLAYSURF.blit(bg, (0, 0))
    scores = font_small.render("Score: " + str(SCORE), True, (0, 0, 0))
    coin_score = font_small.render("Coins: " + str(SCORE2), True, (0, 0, 0))
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_score, (SCREEN_WIDTH - 200, 10))
    for entity in all_sprites:
        if entity != P1:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
    DISPLAYSURF.blit(P1.image, P1.rect)
    P1.move()
    #ADDING SOUNDSS
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("sounds/ss.mp3").play()
        time.sleep(0.5)
        DISPLAYSURF.blit(game_over, (250, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pygame.quit()
        sys.exit()
    collisions = pygame.sprite.spritecollide(P1, all_sprites, True)
    #SC
    for coin in collisions:
        SCORE2 += 1
    pygame.display.update()
    time1.tick(fps)
