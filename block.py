import pygame
from utilities import *


class Block(pygame.sprite.Sprite):
    def __init__(self, img, coord):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load(img, (TILE, TILE))
        self.x, self.y = coord
        self.rect = pygame.Rect(self.x, self.y, TILE, TILE)