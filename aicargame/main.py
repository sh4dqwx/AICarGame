import pygame
from pygame import Vector2
from random import randint

from aicargame.objects.player import Player
from aicargame.objects.enemy import Enemy

WIN_X = 600
WIN_Y = 600
FIRST_LANE_ENEMY_POSITION = Vector2(WIN_X / 6, -100)
SECOND_LANE_ENEMY_POSITION = Vector2(WIN_X / 2, -100)
THIRD_LANE_ENEMY_POSITION = Vector2(WIN_X * 5 / 6, -100)

pygame.init()

win = pygame.display.set_mode((WIN_X, WIN_Y))

enemyTimer = 5000

pygame.display.set_caption("AICarGame")

obj = Player(Vector2(50, 50), Vector2(100, 100))

all_sprites = pygame.sprite.Group()
all_sprites.add(obj)

def spawnEnemy():
    rand = randint(0, 2)
    if(rand == 0):
        newEnemy = Enemy(FIRST_LANE_ENEMY_POSITION, Vector2(100, 100))
    elif(rand == 1):
        newEnemy = Enemy(SECOND_LANE_ENEMY_POSITION, Vector2(100, 100))
    else:
        newEnemy = Enemy(THIRD_LANE_ENEMY_POSITION, Vector2(100, 100))

    all_sprites.add(newEnemy)

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if(enemyTimer >= 1000):
        spawnEnemy()
        enemyTimer = 0
    enemyTimer += 10

    win.fill((0, 0, 0))

    all_sprites.update()
    all_sprites.draw(win)

    pygame.display.update()

pygame.quit()
