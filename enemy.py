import pygame
from utilities import *
from player import Player
from bullet import Bullet
import time
from buff import Buff

ANIM_SPEED = 6


class Enemy(pygame.sprite.Sprite):
    def __init__(self, coord, img, hp):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(coord, (TILE, TILE))
        self.image = image_load(img)
        self.hp = hp
        self.vx, self.vy = 0, 0
        self.dv = ENEMY_SPEED
        self.name = 'enemy'
        self.time = time.time()
        self.radius = 0
        self.die = False
        self.cd_time = 0

    def update(self, player, player_group, blocks, buffs, screen):
        if self.hp == SPIDER_HP:
            return
        self.radius = 5 * TILE
        if pygame.sprite.collide_circle(self, player):
            self.move_x(player)
            self.check_collide_x(blocks, player_group, player)
            self.move_y(player)
            self.check_collide_y(blocks, player_group, player)

        else:
            self.vx, self.vy = 0, 0
        self.radius = 0
        if time.time() - self.cd_time > 1 and pygame.sprite.spritecollide(self, player_group, False):
            self.time = time.time()
            player.get_dmg(ENEMY_DMG)
            # self.kill()

        # self.check_collides(blocks, player_group, player)

        # if time.time() - self.time > 0.6:
        #     self.time = time.time()
        #     self.shoot(player)

        if self.hp <= 0:
            self.kill()
            if get_percentages(100):
                buff = Buff(self.rect.x, self.rect.y)
                buffs.add(buff)

    def get_dmg(self, dmg):
        self.hp -= dmg

    def check_collide_x(self, blocks, player_group, player):
        collided_blocks = pygame.sprite.spritecollide(self, blocks, False)
        for i in collided_blocks:
            if self.vx > 0:
                self.rect.right = i.rect.left
                self.vx = 0
            if self.vx < 0:
                self.rect.left = i.rect.right
                self.vx = 0

    def check_collide_y(self, blocks, player_group, player):
        collided_blocks = pygame.sprite.spritecollide(self, blocks, False)
        for i in collided_blocks:
            if self.vy > 0:
                self.rect.bottom = i.rect.top
                self.vy = 0
            if self.vy < 0:
                self.rect.top = i.rect.bottom
                self.vy = 0

    def get_hp(self):
        return self.hp

    def move_x(self, player):
        if player.rect.x >= self.rect.x:
            self.vx = self.dv
        elif player.rect.x < self.rect.x:
            self.vx = -self.dv
        self.rect.x += self.vx

    def move_y(self, player):
        if player.rect.y >= self.rect.y:
            self.vy = self.dv
        elif player.rect.y < self.rect.y:
            self.vy = -self.dv
        self.rect.y += self.vy

    def shoot(self, player):
        coord = self.rect.x, self.rect.y
        vx, vy = 0, 0
        vx = -(self.rect.x - player.rect.x) // 100
        vy = -(self.rect.y - player.rect.y) // 100

        bullet = Bullet(coord, vx, vy, self)
        player.bullet_group.add(bullet)

    def set_radius(self, radius):
        self.radius = radius
