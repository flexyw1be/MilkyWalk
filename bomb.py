import pygame
from config import *
from utilities import *


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, affination):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load(BOMB)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.clock = pygame.time.Clock()
        self.time = self.clock.tick()

    def update(self):
        time = self.clock.tick()
        print(time - self.time)
        if self.time > 300:
            self.kill()

