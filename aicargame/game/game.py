import time

import pygame
from pygame import Vector2

from aicargame.globals import WINDOW_HEIGHT, WINDOW_WIDTH, ENEMY_INTERVAL
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy


class Game:
    sprites = pygame.sprite.Group()
    window: pygame.Surface

    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AICarGame")

        obj = Player(Vector2(50, 50), Vector2(100, 100))

        self.sprites.add(obj)

    def update(self):
        cur_time = time.time()

        if(cur_time - Enemy.timer >= ENEMY_INTERVAL):
            self.sprites.add(Enemy.spawnEnemy())
            Enemy.timer = cur_time

        self.window.fill((0, 0, 0))
        self.sprites.update()
        self.sprites.draw(self.window)
