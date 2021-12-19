import pygame
from random import choice, randint

from config import *
from utilities import *


class Buff(pygame.sprite.Sprite):
    def __init__(self, x, y, size=(TILE, TILE)):
        pygame.sprite.Sprite.__init__(self)
        self.images = {'heart': [image_load(f'data/heart{i}.png', (TILE // 2, TILE // 2)) for i in range(1, 3)],
                       'bomb': [image_load(f'data/bomb{i}.png', (TILE // 2, TILE // 2)) for i in range(1, 3)],
                       'coin': [image_load(f'data/coin{i}.png', (TILE // 2, TILE // 2)) for i in range(1, 3)]}
        self.name = choice(list(self.images.keys()))
        self.image = self.images[self.name][0]
        self.rect = pygame.Rect(x, y, size[0], size[1])
        self.hp_boost, self.dmg = BOOSTS[self.name]
        self.anim_count = 0

    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            if player.get_hp() == 100 and self.hp_boost > 0:
                if player.vx > 0:
                    self.rect.left = player.rect.right
                if player.vx < 0:
                    self.rect.right = player.rect.left
            else:
                player.set_hp(self.hp_boost)
                self.kill()
            if self.name == 'bomb':
                player.set_bombs()
            if self.name == 'key':
                player.set_key()
            if self.name == 'coin':
                player.set_money(1)
        if pygame.sprite.collide_rect(self, player):
            if player.vy > 0:
                self.rect.top = player.rect.bottom
            elif player.vy < 0:
                self.rect.bottom = player.rect.top
        if self.rect.left < GAME_SIZE.left + TILE:
            self.rect.left = GAME_SIZE.left + TILE
        if self.anim_count >= len(self.images[f'{self.name}']) * ANIM_SPEED:
            self.anim_count = 0
        self.image = self.images[f'{self.name}'][self.anim_count // ANIM_SPEED]
        self.anim_count += 1
