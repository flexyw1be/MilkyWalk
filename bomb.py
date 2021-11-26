import pygame
from config import *
from utilities import *
import time


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, affination):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load(BOMB, (192, 192))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
        self.clock = pygame.time.Clock()
        self.time = time.time()
        self.animation_set = [image_load(f"data/boom{i}.png") for i in range(0, 2)]
        self.i = 0

    def update(self, enemies, bullets):
        collided_blocks = pygame.sprite.spritecollide(self, bullets, False)
        for i in collided_blocks:
            if i.vy > 0:
                self.rect.y += TILE
            elif i.vy < 0:
                self.rect.y -= TILE
            elif i.vx > 0:
                self.rect.x += TILE
            elif i.vx < 0:
                self.rect.x -= TILE
            i.kill()
        if time.time() - self.time > 3:
            collided_blocks = pygame.sprite.spritecollide(self, enemies, False)
            for i in collided_blocks:
                i.get_dmg(BOMB_DMG)

            self.kill()
