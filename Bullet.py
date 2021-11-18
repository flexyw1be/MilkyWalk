import pygame


from config import *
from utilities import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, cooords, vx, vy, affiliation):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(cooords, PLAYER_SIZE)
        self.image = image_load(BULLET, (32, 32))
        self.affination = affiliation
        self.vx, self.vy = vx, vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy



