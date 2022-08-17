import pygame
from pygame import Vector2

from aicargame.objects.player import Player
from aicargame.objects.enemy import Enemy

pygame.init()

win = pygame.display.set_mode((500, 500))

enemyTimer = 5000

pygame.display.set_caption("AICarGame")

obj = Player(Vector2(50, 50), Vector2(100, 100))

all_sprites = pygame.sprite.Group()
all_sprites.add(obj)

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if(enemyTimer >= 1000):
        newEnemy = Enemy(Vector2(400, -70), Vector2(70, 70), None, (255, 0, 0))
        all_sprites.add(newEnemy)
        enemyTimer = 0
    enemyTimer += 10

    win.fill((0, 0, 0))

    all_sprites.update()
    all_sprites.draw(win)

    pygame.display.update()

pygame.quit()
