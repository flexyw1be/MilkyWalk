import pygame

from config import *
from utilities import *
import time


class Bullet(pygame.sprite.Sprite):
    def __init__(self, coords, vx, vy, affiliation):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(coords, PLAYER_SIZE)
        self.image = image_load(BULLET, (32, 32))
        self.affination = affiliation
        self.vx, self.vy = vx, vy
        self.time = time.time()

    def update(self, heroes):
        self.rect.x += self.vx
        self.rect.y += self.vy

        collided_blocks = pygame.sprite.spritecollide(self, heroes, False)
        for i in collided_blocks:
            i.get_dmg(15)
            self.kill()
