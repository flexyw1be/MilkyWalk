import pygame
from config import *
from utilities import *
import time


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, affination):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load(BOMB, (192, 192))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.clock = pygame.time.Clock()
        self.time = time.time()
        self.animation_set = [image_load(f"data/boom{i}.png") for i in range(0, 2)]
        self.i = 0

    def update(self):
        if time.time() - self.time > 3:
            self.kill()

