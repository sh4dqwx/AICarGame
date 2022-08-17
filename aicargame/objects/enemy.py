import pygame
from pygame import Vector2

from aicargame.objects.drawableobject import DrawableObject
from aicargame.textures.textures import Textures

class Enemy(DrawableObject):
    def __init__(self, position: Vector2, size: Vector2):
        super().__init__(position, size, Textures.ENEMY)
        self.__velocity = 5
    
    def update(self):
        self.rect.move_ip((0, self.__velocity))
        win_x, win_y = pygame.display.get_window_size()
        if(self.rect.bottom > win_y):
            self.kill()