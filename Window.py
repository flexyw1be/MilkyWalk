import pygame
from config import *
from utilities import *
from Player import Player


class Window():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIN_SIZE.width, WIN_SIZE.height))
        self.running = True
        self.back = image_load(BACKGROUND, (WIN_SIZE.width, WIN_SIZE.height))
        self.all_blocks = pygame.sprite.Group()
        self.player = Player()
        self.player.add(self.all_blocks)

    def run(self):
        self.running = True
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.screen.blit(self.back, (0, 0))
            # self.all_blocks.draw(self.screen)

            pygame.display.flip()
