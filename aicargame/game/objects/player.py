import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.textures.textures import Textures
from aicargame.globals import (
    PLAYER_VELOCITY,
    PLAYER_SIZE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

PLAYER_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.9)
PLAYER_SIZE = Vector2(WINDOW_WIDTH, WINDOW_WIDTH * 0.9) * PLAYER_SIZE
PLAYER_VELOCITY = WINDOW_WIDTH * PLAYER_VELOCITY

class Player(DrawableObject):
    def __init__(self, position: Vector2 = PLAYER_START):
        super().__init__(position, PLAYER_SIZE, Textures.PLAYER)
        self.__velocity = PLAYER_VELOCITY

    def update(self):
        keys = pygame.key.get_pressed()

        vec = Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            vec.x -= self.__velocity

        if keys[pygame.K_RIGHT]:
            vec.x += self.__velocity

        self.rect.move_ip(vec)

        self._keep_inside()

    def _keep_inside(self):
        if self.rect.left < WINDOW_WIDTH * 0.02:
            self.rect.left = WINDOW_WIDTH * 0.02

        if self.rect.right > WINDOW_WIDTH * 0.98:
            self.rect.right = WINDOW_WIDTH * 0.98

    def reset(self):
        self.rect.center = PLAYER_START
