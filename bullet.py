import pygame

from config import *
from utilities import *
import time


class Bullet(pygame.sprite.Sprite):
    def __init__(self, coords, vx, vy, affiliation, size=(TILE // 2, TILE // 2)):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(coords, size)
        self.image = image_load(BULLET, size)
        self.affination = affiliation
        self.vx, self.vy = vx, vy
        self.time = time.time()
        self.die = False

    def update(self, heroes, player, blocks, screen):
        self.rect.y += self.vy
        if not self.die  and (not (GAME_SIZE.x + TILE < self.rect.x < GAME_SIZE.right - TILE) or not (TILE * 2 < self.rect.y < TILE * 12))\
                :
            self.die = True
            self.time = time.time()
            self.vx, self.vy = 0, 0
        self.rect.x += self.vx

        for i in blocks:
            if pygame.sprite.collide_rect(self, i) and not self.die:
                self.die = True
                self.time = time.time()
                self.vx, self.vy = 0, 0
                # self.kill()
                # self.image = image_load(BULLET_DIE, (40, 40))
        collided_heroes = []
        if not self.die:
            collided_heroes = pygame.sprite.spritecollide(self, heroes, False)
        print(collided_heroes)
        for i in collided_heroes:
            if i.name != self.affination:
                print(i.name, self.affination)
                i.get_dmg(BULLET_DMG)
                self.die = True
                self.time = time.time()
                self.vx, self.vy = 0, 0

        if self.die and self.time - time.time() > -0.05:
            self.image = image_load(BULLET_DIE, (40, 40))
            # self.time = time.time()
        if self.die and not self.time - time.time() > -0.05:
            print(1)
            self.kill()
