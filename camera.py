import pygame
from config import *


class Camera:
    def __init__(self):
        pygame.init()

        self.rect = pygame.Rect((0, 0), (WIN_SIZE.width, WIN_SIZE.height))
        self.vx, self.vy = 0, 0

    def update(self, player_x, player_y):
        self.rect.centerx = player_x
        self.rect.centery = player_y

    def draw(self, screen, blocks):
        for block in blocks:
            screen.blit(block.image, (block.rect.x - self.rect.x, block.rect.y - self.rect.y))
