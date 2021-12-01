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

    def update(self, heroes, player, blocks):
        self.rect.x += self.vx
        if not GAME_SIZE.x + TILE < self.rect.x < GAME_SIZE.right - TILE or not TILE * 2 < self.rect.y < TILE * 12:
            self.kill()
        # if not TILE * 2 < self.rect.y < TILE * 12:
        #     self.kill()

        self.rect.y += self.vy

        collided_heroes = pygame.sprite.spritecollide(self, heroes, False)
        for i in collided_heroes:
            if i != self.affination:
                i.get_dmg(BULLET_DMG)
                self.kill()

