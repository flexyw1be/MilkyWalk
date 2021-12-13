import pygame

from config import *
from utilities import *
import time
from bullet import Bullet


class Boss(pygame.sprite.Sprite):
    def __init__(self, coord):
        pygame.sprite.Sprite.__init__(self)
        x, y = coord
        self.hp, self.dmg, self.bullet_dmg = [BOSS[x] for x in list(BOSS.keys())]
        self.image = image_load(BOSS_IMAGE, PLAYER_SIZE)
        self.rect = pygame.Rect((x, y), PLAYER_SIZE)
        self.time = time.time()
        self.shoot_time = 0
        self.name = 'boss'
        self.jump_time = 0
        self.stage = 2
        self.vx, self.vy = 0, 0

    def update(self, player, bullet_group, blocks, screen):
        pygame.draw.rect(screen, 'red',
                         (TILE * 2, GAME_SIZE.bottom - TILE + TILE // 2, self.hp * TILE * 16 / BOSS['hp'], 50))

        pygame.draw.rect(screen, 'black',
                         (TILE * 2, GAME_SIZE.bottom - TILE + TILE // 2, GAME_SIZE.right - TILE * 3, 50), 1)
        if time.time() - self.time > 4:
            if self.stage == 1:
                self.stage = 2
            else:
                self.stage = 1
                self.vx, self.vy = 0, 0
            self.time = time.time()
        if self.stage == 1:
            self.shooting_stage(player, bullet_group)
        elif self.stage == 2:
            self.running_stage(player)
        self.rect.x += self.vx
        collided_blocks = pygame.sprite.spritecollide(self, blocks, False)
        for i in collided_blocks:
            if self.vx > 0:
                self.rect.right = i.rect.left
                self.vx = 0
            if self.vx < 0:
                self.rect.left = i.rect.right
                self.vx = 0
        if not self.rect.left > GAME_SIZE.left + TILE:
            self.rect.left = GAME_SIZE.left + TILE
        if not self.rect.right < GAME_SIZE.right - TILE:
            self.rect.right = GAME_SIZE.right - TILE
        self.rect.y += self.vy
        collided_blocks = pygame.sprite.spritecollide(self, blocks, False)
        for i in collided_blocks:
            if self.vy > 0:
                self.rect.bottom = i.rect.top
                self.vy = 0
            if self.vy < 0:
                self.rect.top = i.rect.bottom
                self.vy = 0
        if not self.rect.top > GAME_SIZE.top + TILE:
            self.rect.top = GAME_SIZE.top + TILE
        if not self.rect.bottom < GAME_SIZE.bottom - TILE:
            self.rect.bottom = GAME_SIZE.bottom - TILE

    def shooting_stage(self, player, bullet_group):
        if time.time() - self.shoot_time > 1:
            self.shoot(player, bullet_group)
            self.shoot_time = time.time()

    def running_stage(self, player):
        if time.time() - self.jump_time > 1:
            self.jump_time = time.time()
            leg_x, leg_y = (player.rect.centerx - self.rect.centerx), (
                    player.rect.centery - self.rect.centery)
            gip = (leg_x ** 2 + leg_y ** 2) ** 0.5
            self.vy, self.vx = (leg_y / gip * PLAYER_SPEED), (leg_x / gip * PLAYER_SPEED)

    def shoot(self, player, bullet_group):
        leg_x, leg_y = (player.rect.centerx - self.rect.centerx), (
                player.rect.centery - self.rect.centery)
        gip = (leg_x ** 2 + leg_y ** 2) ** 0.5
        vy, vx = (leg_y / gip * BOSS_BULLET_SPEED), (leg_x / gip * BOSS_BULLET_SPEED)
        bullet = Bullet((self.rect.centerx, self.rect.centery), vx, vy, self.name)
        bullet.add(player.bullet_group)

    def get_dmg(self, dmg):
        self.hp -= dmg


