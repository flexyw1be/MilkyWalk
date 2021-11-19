import pygame
from utilities import *


class Block(pygame.sprite.Sprite):
    def __init__(self, img, coord):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load(img)
        self.rect = pygame.Rect(coord, self.image.get_rect())