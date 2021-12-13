import pygame
from config import *
from utilities import *
from check_bomb import CheckBomb
from random import choice
import time


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, affination):
        pygame.sprite.Sprite.__init__(self)
        self.images = {
            'boom0': image_load('data/boom0.png', PLAYER_SIZE),
            'boom1': image_load('data/boom1.png', PLAYER_SIZE)
        }
        self.image = image_load(BOMB, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
        self.clock = pygame.time.Clock()
        self.time = time.time()
        self.animation_set = [image_load(f"data/boom{i}.png") for i in range(0, 2)]
        self.current_time = 0
        self.i = 0
        self.radius = TILE * 3
        self.boom = False

    def update(self, heroes, bullets, blocks, screen):
        collided_blocks = pygame.sprite.spritecollide(self, bullets, False)
        pygame.draw.circle(screen, 'black', (self.rect.centerx, self.rect.centery), self.radius, 3)
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
            self.image = self.images[choice(list(self.images.keys()))]
            self.current_time = time.time()
            self.time = time.time()
            self.boom = True
            for i in blocks:
                if pygame.sprite.collide_circle(self, i):
                    i.set_hp(i.get_hp() - BOMB_DMG)
            for i in heroes:
                if pygame.sprite.collide_circle(self, i):
                    i.get_dmg(BOMB_DMG)


        if time.time() - self.current_time > 0.5 and self.boom:
            self.kill()
            # for i in enemies:
            #     if bomb.check_collide(i):
            #         i.get_dmg(BOMB_DMG)
            #         self.kill()

            # self.kill()
