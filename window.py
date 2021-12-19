import pygame
from config import *
from utilities import *
from player import Player
from enemy import Enemy
from block import Block
from boss import Boss
from random import choice


class Window:
    def __init__(self):
        pygame.init()
        self.map_sprites = MAPS_SPRITES
        self.screen = pygame.display.set_mode((WIN_SIZE.width, WIN_SIZE.height))
        self.running = True
        self.back = image_load(BACKGROUND, (GAME_SIZE.width + TILE * 2, GAME_SIZE.height + TILE * 2))
        self.player = Player()
        self.all_blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.heroes = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()
        for i in ROOM_LIST:
            for j in i:
                if j != 0:
                    self.map_sprites[j] = self.load_map(j)
        # self.player.add(self.heroes)
        self.bullet_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.bombs_group = pygame.sprite.Group()
        self.running = True
        self.player_group = pygame.sprite.Group()
        self.player.add(self.player_group)
        self.buffs = pygame.sprite.Group()
        self.hp_images = {
            "100hp": 'data/fullhp.png',
            "87hp": 'data/87hp.png',
            "65hp": 'data/65hp.png',
            "50hp": 'data/50hp.png',
            "37hp": 'data/37hp.png',
            "25hp": 'data/25hp.png',
            "12hp": 'data/12hp.png',
            '75hp': 'data/75hp.png'

        }

        self.counts_images = {
            '1': image_load('data/1.png'),
            '2': image_load('data/2.png'),
            '3': image_load('data/3.png'),
            '4': image_load('data/4.png'),
            '5': image_load('data/5.png'),
            '6': image_load('data/6.png'),
            '7': image_load('data/7.png'),
            '8': image_load('data/8.png'),
            '9': image_load('data/9.png'),
            '0': image_load('data/0.png')

        }
        self.hp_hud = image_load(self.hp_images['100hp'], (TILE * 4, TILE))
        self.bomb = image_load(BOMB)

        self.map = SPAWN_ROOM

    def run(self):
        self.load_map(self.map)
        self.player.add(self.heroes)
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.screen.blit(self.back, (0, 0))

            if self.player.get_hp() > 0:
                self.hp_hud = image_load(self.hp_images[f'{self.player.get_hp()}hp'], (TILE * 4, TILE))
            for i in self.enemies:
                i.add(self.heroes)
            # for i in self.bosses:
            #     i.add(self.heroes)
            self.set_bullet_group()
            self.set_bombs_group()
            self.all_blocks, self.enemies, self.bosses = self.map_sprites[self.player.map]
            self.player.update(self.all_blocks, self.buffs)
            self.enemies.update(self.player, self.player_group, self.all_blocks, self.buffs, self.screen)
            self.bosses.update(self.player, self.bullet_group, self.all_blocks, self.screen)
            self.all_blocks.update(self.player, self.buffs)
            self.bombs_group.update(self.heroes, self.bullet_group, self.all_blocks, self.screen)
            self.bullet_group.update(self.heroes, self.player, self.all_blocks, self.screen)

            self.buffs.update(self.player)

            self.all_blocks.draw(self.screen)

            self.player_group.draw(self.screen)
            self.bombs_group.draw(self.screen)

            self.bullet_group.draw(self.screen)
            self.buffs.draw(self.screen)
            self.enemies.draw(self.screen)
            for i in self.enemies:
                pygame.draw.rect(self.screen, 'red', (i.rect.x, i.rect.y - 20, i.hp * TILE // ENEMY_HP, 10))
                pygame.draw.rect(self.screen, 'black', (i.rect.x, i.rect.y - 20, TILE, 10), 2)
            self.bosses.draw(self.screen)
            self.draw_map()


            self.clock.tick(FPS)
            pygame.display.flip()

    def set_bullet_group(self):
        self.bullet_group = self.player.get_bullet_group()

    def set_bombs_group(self):
        self.bombs_group = self.player.get_bombs_group()

    def load_map(self, path):
        self.all_blocks.empty()
        self.enemies.empty()
        self.bosses.empty()
        self.heroes.empty()
        with open(path, 'r', encoding='utf-8') as file:
            for y, line in enumerate(file):
                for x, letter in enumerate(line):
                    coord = x * TILE, y * TILE
                    if letter == 'S':
                        # [f'data/stone{i}.png' for i in range(0, 3)]
                        block = Block(choice([f'data/stone{i}.png' for i in range(0, 3)]), coord, name='stone')
                        block.add(self.all_blocks)
                    if letter == 'P':
                        self.player.rect.x, self.player.rect.y = coord
                    if letter == 'E':
                        enemy = Enemy(coord, ENEMY_IDLE, 100)
                        self.enemies.add(enemy)
                    if letter == 'C':
                        block = Block(CHEST, coord, (TILE * 2, TILE * 2), 'chest')
                        block.add(self.all_blocks)
                    if letter == 'B':
                        boss = Boss(coord)
                        boss.add(self.bosses)
                        boss.add(self.heroes)
            return self.all_blocks, self.enemies, self.bosses

    def draw_map(self):
        pygame.draw.rect(self.screen, '#8B4513', (WIN_SIZE.right // 2 - 64, 16, 32 * 3, 32 * 3))
        pygame.draw.rect(self.screen, 'black', (WIN_SIZE.right // 2 - 64, 16, 32 * 3, 32 * 3), 2)
        for i, y in enumerate(MAP_IMAGES):
            for j, x in enumerate(y):
                if x != 0:
                    self.screen.blit(image_load(x, (32, 32)), (WIN_SIZE.right // 2 - 64 + j * 32, 16 + i * 32))
        self.screen.blit(self.hp_hud, (0, 0))
        self.screen.blit(self.bomb, (30, 60))
        self.screen.blit(self.counts_images[f'{self.player.bombs}'], (90, 60))
