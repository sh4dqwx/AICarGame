import time
from random import randint

import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.textures.textures import Textures
from aicargame.globals import (
    WINDOW_HEIGHT,
    ENEMY_VELOCITY,
    FIRST_LANE,
    SECOND_LANE,
    THIRD_LANE
)

class Enemy(DrawableObject):
    timer = time.time()

    def __init__(self, position: Vector2, size: Vector2):
        super().__init__(position, size, Textures.ENEMY)
        self.__velocity = ENEMY_VELOCITY
    
    def update(self):
        self.rect.move_ip((0, self.__velocity))
        if(self.rect.bottom > WINDOW_HEIGHT):
            self.kill()

    @staticmethod
    def spawnEnemy():
        rand = randint(0, 2)
        if(rand == 0):
            newEnemy = Enemy(FIRST_LANE, Vector2(100, 100))
        elif(rand == 1):
            newEnemy = Enemy(SECOND_LANE, Vector2(100, 100))
        else:
            newEnemy = Enemy(THIRD_LANE, Vector2(100, 100))

        return newEnemy
