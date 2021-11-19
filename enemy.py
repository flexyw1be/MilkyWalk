import pygame
from utilities import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((0, 0), PLAYER_SIZE)
        self.image = image_load(img, PLAYER_SIZE)

    def update(self):
        pass