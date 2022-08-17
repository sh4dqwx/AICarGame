import pygame
from pygame import Vector2
from random import randint

from aicargame.objects.player import Player
from aicargame.objects.enemy import Enemy

pygame.init()

win = pygame.display.set_mode((600, 600))

enemyTimer = 5000

pygame.display.set_caption("AICarGame")

obj = Player(Vector2(50, 50), Vector2(100, 100))

all_sprites = pygame.sprite.Group()
all_sprites.add(obj)

run = True

def spawnEnemy():
    rand = randint(0, 2)
    newEnemy = Enemy(Vector2(rand*200+100, -100), Vector2(100, 100))
    all_sprites.add(newEnemy)

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
