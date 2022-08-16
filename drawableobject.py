import pygame
from pygame import Vector2


class DrawableObject(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, size: Vector2, texture=None, color=None):
        if texture is None and color is None:
            raise NotImplementedError

        super().__init__()

        if texture is None:
            self.image = pygame.Surface(size)
            self.image.fill(color)
        else:
            try:
                texture = pygame.image.load(texture)
            except Exception as ex:
                self.image.fill((255, 255, 255))
                print(str(ex))
            else:
                texture = pygame.transform.scale(texture, size)
                self.image = texture

        self.rect = self.image.get_rect()
        self.rect.center = position


class Player(DrawableObject):
    def __init__(self, position: Vector2, size: Vector2, texture):
        super().__init__(position, size, texture)
        self.__velocity = 10
        self.__x_border = 10
        self.__y_border = 10

    def update(self):
        keys = pygame.key.get_pressed()

        vec = Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            vec.x -= self.__velocity

        if keys[pygame.K_RIGHT]:
            vec.x += self.__velocity

        if keys[pygame.K_UP]:
            vec.y -= self.__velocity

        if keys[pygame.K_DOWN]:
            vec.y += self.__velocity

        self.rect.move_ip(vec)

        self._keep_inside()

    def _keep_inside(self):
        win_x, win_y = pygame.display.get_window_size()

        win_x_border = win_x / self.__x_border
        win_y_border = win_y / self.__y_border

        if self.rect.centerx < win_x_border:
            self.rect.centerx = win_x_border

        if self.rect.centerx > win_x - win_x_border:
            self.rect.centerx = win_x - win_x_border

        if self.rect.centery < win_y_border:
            self.rect.centery = win_y_border

        if self.rect.centery > win_y - win_y_border:
            self.rect.centery = win_y - win_y_border
