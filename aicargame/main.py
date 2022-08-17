import pygame
from pygame import Vector2
from random import randint

from aicargame.game.game import Game
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy

pygame.init()

game = Game()

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game.update()
    pygame.display.update()

pygame.quit()
