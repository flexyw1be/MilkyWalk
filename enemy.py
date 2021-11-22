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


        if self.hp <= 0:
            self.kill()

    def get_dmg(self, dmg):
        self.hp -= dmg

    def get_hp(self):
        return self.hp


