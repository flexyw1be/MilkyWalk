import pygame
from config import *
from utilities import *
from bullet import Bullet
from bomb import Bomb
from buff import Buff
import time


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((0, 0), PLAYER_SIZE)
        self.images = {
            'idle': [image_load(f'data/player_idle{i}.png', PLAYER_SIZE) for i in range(1, 4)],
            'left': [image_load(f'data/player_l{i}.png', PLAYER_SIZE) for i in range(1, 4)],
            'up': [image_load(f'data/player_up{i}.png', PLAYER_SIZE) for i in range(1, 4)],
        }

        self.images[f'right'] = [pygame.transform.flip(img, True, False)
                                 for img in self.images[f'left']]
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
        self.keys = 0
        self.damage = 25
        self.keys = 1
        self.dir = 'idle'
        self.name = 'player'
        self.anim_count = 0
        self.state_prev = f'{self.dir}'
        self.state = True
        self.map = SPAWN_ROOM

    def update(self, hard_blocks, buffs):
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
            if i.name == 'chest' and self.keys > 0:
                buff = Buff(i.rect.x, i.rect.y)
                buffs.add(buff)
                i.kill()
            if self.vx > 0:
                self.rect.right = i.rect.left
                self.vx = 0
            elif self.vx < 0:
                self.rect.left = i.rect.right
                self.vx = 0

        if not self.rect.left > GAME_SIZE.left + TILE:
            map_x, map_y = 0, 0
            for x in ROOM_LIST:
                for y in x:
                    if y == self.map:
                        map_x, map_y = x, y
                        break
            # map = map_x[map_x.index(map_y) - 1]
            print(map_x.index(map_y))
            if map_x.index(map_y) > 0:
                if map_x[map_x.index(map_y) - 1] != 0:
                    self.map = map_x[map_x.index(map_y) - 1]
                    self.rect.right = GAME_SIZE.right - TILE * 2 - TILE
                else:
                    self.rect.left = GAME_SIZE.left + TILE
            else:
                self.rect.left = GAME_SIZE.left + TILE
            # self.rect.left = GAME_SIZE.left + TILE
        elif not self.rect.right < GAME_SIZE.right - TILE:
            map_x, map_y = 0, 0
            for x in ROOM_LIST:
                for y in x:
                    if y == self.map:
                        map_x, map_y = x, y
                        break
            if map_x.index(map_y) < 2:
                if map_x[map_x.index(map_y) + 1] != 0:
                    self.map = map_x[map_x.index(map_y) + 1]
                    self.rect.x = GAME_SIZE.left + TILE
                else:
                    self.rect.right = GAME_SIZE.right - TILE
            else:
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
        self.state = False
        if self.vy < 0:
            self.dir = 'up'
        elif self.vx > 0:
            self.dir = 'right'
        elif self.vx < 0:
            self.dir = 'left'
        elif self.vy > 0:
            self.dir = 'idle'
        else:
            self.state = True

        collided_blocks = pygame.sprite.spritecollide(self, hard_blocks, False)
        for i in collided_blocks:
            if i.name == 'chest' and self.keys > 0:
                buff = Buff(i.rect.centerx, i.rect.centery)
                buffs.add(buff)
                self.keys -= 1
                i.kill()
            if self.vy > 0:
                self.rect.bottom = i.rect.top
                self.vy = 0
            elif self.vy < 0:
                self.vy = 0
                self.rect.top = i.rect.bottom

        if not self.rect.top > GAME_SIZE.top + TILE:
            map_x, map_y = 0, 0
            for x in ROOM_LIST:
                for y in x:
                    if y == self.map:
                        map_x, map_y = x, y
                        break
            if ROOM_LIST.index(map_x) > 0:
                if ROOM_LIST[ROOM_LIST.index(map_x) -1][map_x.index(map_y)] !=0:
                    self.map = ROOM_LIST[ROOM_LIST.index(map_x) - 1][map_x.index(map_y)]
                    self.rect.bottom = GAME_SIZE.bottom - TILE
                else:
                    self.rect.top = GAME_SIZE.top + TILE
            else:
                self.rect.top = GAME_SIZE.top + TILE
        elif not self.rect.bottom < GAME_SIZE.bottom - TILE:
            map_x, map_y = 0, 0
            for x in ROOM_LIST:
                for y in x:
                    if y == self.map:
                        map_x, map_y = x, y
                        break
            if ROOM_LIST.index(map_x) > 0:
                if ROOM_LIST[ROOM_LIST.index(map_x) + 1][map_x.index(map_y)] != 0:
                    self.map = ROOM_LIST[ROOM_LIST.index(map_x) + 1][map_x.index(map_y)]
                    self.rect.top = GAME_SIZE.top +TILE
                else:
                    self.rect.bottom = GAME_SIZE.bottom - TILE
            else:
                self.rect.bottom = GAME_SIZE.bottom - TILE

        down_shoot, up_shoot = keys[pygame.K_DOWN], keys[pygame.K_UP]
        right_shoot, left_shoot = keys[pygame.K_RIGHT], keys[pygame.K_LEFT]
        if any([down_shoot, up_shoot, right_shoot, left_shoot]) and time.time() - self.bullets_time > 0.5:
            self.bullets_time = time.time()
            self.shoot(down_shoot, up_shoot, right_shoot, left_shoot)
        set_bomb = keys[pygame.K_e]
        if set_bomb and time.time() - self.bombs_time > 0.5 and self.bombs:
            self.bombs_time = time.time()
            self.set_bomb()
            self.bombs -= 1
        if self.anim_count >= len(self.images[f'{self.dir}']) * ANIM_SPEED:
            self.anim_count = 0
        if not self.state:
            self.image = self.images[f'{self.dir}'][self.anim_count // ANIM_SPEED]
            self.anim_count += 1
        else:
            self.image = self.images['idle'][1]
        self.check_hp(self.hp)

    def shoot(self, down_shoot, up_shoot, right_shoot, left_shoot):
        coords = self.rect.centerx, self.rect.centery
        size = (40, 40)
        if down_shoot:
            bullet = Bullet(coords, 0, BULLET_SPEED, self.name, size)
        if up_shoot:
            bullet = Bullet(coords, 0, -BULLET_SPEED, self.name, size)
        if right_shoot:
            bullet = Bullet(coords, BULLET_SPEED, 0, self.name, size)
        if left_shoot:
            bullet = Bullet(coords, -BULLET_SPEED, 0, self.name, size)
        self.bullet_group.add(bullet)

    def set_bomb(self):
        self.bombs_group.add(Bomb(self.rect.centerx, self.rect.centery, 1))

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp += hp

    def check_hp(self, hp):
        if hp <= 0:
            self.kill()

    def set_key(self):
        self.keys += 1

    def get_dmg(self, dmg):
        self.hp -= dmg

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money += money

    def get_keys(self):
        return self.keys

    def set_keys(self):
        return self.keys

    def set_bombs(self):
        self.bombs += 1

    def get_bombs(self):
        return self.bombs

    def get_bullet_group(self):
        return self.bullet_group

    def get_bombs_group(self):
        return self.bombs_group

    def set_radius(self, radius):
        self.radius = radius
