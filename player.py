import pygame
from config import *
from utilities import *
from bullet import Bullet
from bomb import Bomb
import time


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((0, 0), PLAYER_SIZE)
        self.images = {
            'idle': image_load('data/player_idle.png', PLAYER_SIZE),
            'right': image_load('data/player_r.png', PLAYER_SIZE),
            'left': image_load('data/player_l.png', PLAYER_SIZE),
            'up': image_load('data/player_up.png', PLAYER_SIZE),
        }
        self.image = self.images['idle']
        self.vx, self.vy = 0, 0
        self.money, self.bombs, self.keys = 0, 1, 0
        self.clock = pygame.time.Clock()
        self.bombs_time = time.time()
        self.bullets_time = time.time()
        self.bullet_group = pygame.sprite.Group()
        self.bombs_group = pygame.sprite.Group()
        self.hp = 100
        self.bombs = 2
        self.damage = 25

    def update(self, hard_blocks):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]
        if left and not right:
            self.vx = -PLAYER_SPEED
        elif right and not left:
            self.vx = PLAYER_SPEED
        else:
            self.vx = 0
        self.rect.x += self.vx
        self.image = self.images['idle']

        collided_blocks = pygame.sprite.spritecollide(self, hard_blocks, False)
        for i in collided_blocks:
            if self.vx > 0:
                self.rect.right = i.rect.left
                self.vx = 0
            elif self.vx < 0:
                self.rect.left = i.rect.right
                self.vx = 0

        if not self.rect.left > GAME_SIZE.left + TILE:
            self.rect.left = GAME_SIZE.left + TILE
        if not self.rect.right < GAME_SIZE.right - TILE:
            self.rect.right = GAME_SIZE.right - TILE
        up = keys[pygame.K_w]
        down = keys[pygame.K_s]
        if up and not down:
            self.vy = -PLAYER_SPEED
        elif down and not up:
            self.vy = PLAYER_SPEED
        else:
            self.vy = 0
        self.rect.y += self.vy
        if self.vy <0:
            self.image = self.images['up']
        elif self.vx > 0:
            self.image = self.images['right']
        elif self.vx < 0:
            self.image = self.images['left']

        collided_blocks = pygame.sprite.spritecollide(self, hard_blocks, False)
        for i in collided_blocks:
            if self.vy > 0:
                self.rect.bottom = i.rect.top
                self.vy = 0
            elif self.vy < 0:
                self.vy = 0
                self.rect.top = i.rect.bottom

        if not self.rect.top > GAME_SIZE.top + TILE:
            self.rect.top = GAME_SIZE.top + TILE
        if not self.rect.bottom < GAME_SIZE.bottom - TILE:
            self.rect.bottom = GAME_SIZE.bottom - TILE
        if not TILE < self.rect.x < TILE * 12 or not TILE <= self.rect.y <= TILE * 12:
            pass
        down_shoot, up_shoot = keys[pygame.K_DOWN], keys[pygame.K_UP]
        right_shoot, left_shoot = keys[pygame.K_RIGHT], keys[pygame.K_LEFT]
        if any([down_shoot, up_shoot, right_shoot, left_shoot]) and time.time() - self.bullets_time > 0.5:
            self.bullets_time = time.time()
            self.shoot(down_shoot, up_shoot, right_shoot, left_shoot)
        set_bomb = keys[pygame.K_e]
        if set_bomb and time.time() - self.bombs_time > 0.5 and self.bombs:
            self.bombs_time = time.time()
            self.set_bomb()
            self.bombs -=1

        self.check_hp(self.hp)

    def shoot(self, down_shoot, up_shoot, right_shoot, left_shoot):
        coords = self.rect.centerx, self.rect.centery
        if down_shoot:
            bullet = Bullet(coords, 0, BULLET_SPEED, self)
        if up_shoot:
            bullet = Bullet(coords, 0, -BULLET_SPEED, self)
        if right_shoot:
            bullet = Bullet(coords, BULLET_SPEED, 0, self)
        if left_shoot:
            bullet = Bullet(coords, -BULLET_SPEED, 0, self)
        self.bullet_group.add(bullet)

    def set_bomb(self):
        self.bombs_group.add(Bomb(self.rect.centerx, self.rect.centery, 1))

    def get_hp(self):
        return self.hp

    def check_hp(self, hp):
        if hp <= 0:
            self.kill()

    def get_dmg(self, dmg):
        self.hp -= dmg

    def get_money(self):
        return self.money

    def get_keys(self):
        return self.keys

    def get_bombs(self):
        return self.bombs

    def get_bullet_group(self):
        return self.bullet_group

    def get_bombs_group(self):
        return self.bombs_group
