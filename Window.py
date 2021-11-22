import pygame
from utilities import *
from player import Player
from enemy import Enemy
from block import Block


class Window:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIN_SIZE.width, WIN_SIZE.height))
        self.running = True
        self.back = image_load(BACKGROUND, (WIN_SIZE.width, WIN_SIZE.height))
        self.all_blocks = pygame.sprite.Group()
        self.player = Player()
        self.player.add(self.all_blocks)
        self.heroes = pygame.sprite.Group()
        self.player.add(self.heroes)
        self.bullet_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.bombs_group = pygame.sprite.Group()
        self.running = True
        self.enemy = Enemy('data/bee.png', 100)
        self.enemies = pygame.sprite.Group()
        self.enemy.add(self.enemies)

        self.map = SPAWN_MAP

    def run(self):
        # self.load_map()
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.screen.blit(self.back, (0, 0))
            for i in self.enemies:
                i.add(self.heroes)
            self.set_bullet_group()
            self.set_bombs_group()
            self.all_blocks.update()
            self.enemies.update(self.player)
            self.bombs_group.update(self.heroes, self.bullet_group)
            self.bullet_group.update(self.enemies)

            self.all_blocks.draw(self.screen)
            self.bombs_group.draw(self.screen)
            self.bullet_group.draw(self.screen)
            self.enemies.draw(self.screen)

            self.clock.tick(FPS)
            pygame.display.flip()

    def set_bullet_group(self):
        self.bullet_group = self.player.get_bullet_group()

    def set_bombs_group(self):
        self.bombs_group = self.player.get_bombs_group()

    def load_map(self):
        self.player.money = 0
        self.all_blocks.empty()
        self.player.add(self.all_blocks)
        with open(self.map, 'r', encoding='utf-8') as file:
            for y, line in enumerate(file):
                for x, letter in enumerate(line):
                    coord = x * TILE, y * TILE
                    if letter == 'D':
                        block = Block(DOOR_X, coord)
                        block.add(self.all_blocks)
                    if letter == 'M':
                        block = Block(DOOR_Y, coord)
                        block.add(self.all_blocks)
