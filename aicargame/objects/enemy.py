import pygame
from pygame import Vector2

from aicargame.objects.drawableobject import DrawableObject

class Enemy(DrawableObject):
    def __init__(self, position: Vector2, size: Vector2, texture=None, color=None):
        super().__init__(position, size, texture, color)
        self.__velocity = 3
    
    def update(self):
        self.rect.move_ip((0, self.__velocity))
        if(self.rect.bottom > 500):
            self.kill()