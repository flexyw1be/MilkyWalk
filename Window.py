import pygame
from utilities import *
from player import Player


class Window:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIN_SIZE.width, WIN_SIZE.height))
        self.running = True
        self.back = image_load(BACKGROUND, (WIN_SIZE.width, WIN_SIZE.height))
        self.all_blocks = pygame.sprite.Group()
        self.player = Player()
        self.player.add(self.all_blocks)
        self.bullet_group = pygame.sprite.Group()

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
            self.set_bullet_group()
            self.all_blocks.update()
            self.all_blocks.draw(self.screen)

            pygame.display.flip()

    def set_bullet_group(self):
        self.bullet_group = self.player.get_bullet_group()
        for i in self.bullet_group:
            i.add(self.all_blocks)



game = Window()
game.run()