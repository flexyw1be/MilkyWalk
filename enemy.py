import pygame
from utilities import *
from player import Player
from bullet import Bullet
import time

ANIM_SPEED = 6


class Enemy(pygame.sprite.Sprite):
    def __init__(self, coord, img, hp):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(coord, PLAYER_SIZE)
        self.image = image_load(img)
        self.hp = hp
        self.vx, self.vy = 0, 0
        self.dv = PLAYER_SPEED // 4
        self.time = time.time()

    def update(self, player, player_group):
        if player.rect.x >= self.rect.x:
            self.vx = self.dv
        elif player.rect.x < self.rect.x:
            self.vx = -self.dv
        if player.rect.y >= self.rect.y:
            self.vy = self.dv
        elif player.rect.y < self.rect.y:
            self.vy = -self.dv
        self.rect.x += self.vx
        self.rect.y += self.vy

        collided_players = pygame.sprite.spritecollide(self, player_group, False)
        for i in collided_players:
            i.get_dmg(ENEMY_DMG)
            self.kill()
        if time.time() - self.time > 0.6:
            self.time = time.time()
            self.shoot(player)
        if self.hp <= 0:
            self.kill()

    def get_dmg(self, dmg):
        self.hp -= dmg

    def get_hp(self):
        return self.hp

    def shoot(self, player):
        coord = self.rect.x, self.rect.y
        vx, vy = 0, 0
        vx = -(self.rect.x - player.rect.x) // 100
        vy = -(self.rect.y - player.rect.y) // 100

        bullet = Bullet(coord, vx, vy, self)
        player.bullet_group.add(bullet)
