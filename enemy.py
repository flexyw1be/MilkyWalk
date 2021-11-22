import pygame
from utilities import *
from player import Player
import time


class Enemy(pygame.sprite.Sprite):
    def __init__(self, img, hp):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((100, 100), PLAYER_SIZE)
        self.image = image_load(img, PLAYER_SIZE)
        self.hp = hp
        self.vx, self.vy = 0, 0
        self.time = time.time()

    def update(self, player):
        if player.rect.x >= self.rect.x:
            self.vx = PLAYER_SPEED // 3
        elif player.rect.x < self.rect.x:
            self.vx = -PLAYER_SPEED // 3
        elif self.rect.x == self.rect.x:
            self.vx = 0
        if player.rect.y >= self.rect.y:
            self.vy = PLAYER_SPEED // 3
        elif player.rect.y < self.rect.y:
            self.vy = -PLAYER_SPEED // 3
        elif self.rect.y == self.rect.y:
            self.vy = 0

        self.rect.x += self.vx
        self.rect.y += self.vy

        collided_blocks = pygame.sprite.spritecollide(self, player.bullet_group, False)
        if collided_blocks and time.time() - self.time > 0.5:
            self.time = time.time()
            self.hp -= 12.5
            for i in collided_blocks:
                i.kill()

        if self.hp <= 0:
            self.kill()


