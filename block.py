import pygame
from utilities import *


class Block(pygame.sprite.Sprite):
    def __init__(self, img, coord, size=(TILE, TILE), name=''):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load(img, size)
        self.x, self.y = coord
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.name = name
        self.hp = 1

    def update(self):
        if self.get_hp() < 1:
            self.kill()

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp
