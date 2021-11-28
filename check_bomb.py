import pygame
from config import *


class CheckBomb(pygame.sprite.Sprite):
    def __init__(self, coord):
        x, y = coord
        self.rect = pygame.Rect(x - TILE, y - TILE, 192, 192)

    def check_collide(self, block):
        return pygame.Rect.colliderect(self.rect, block.rect)
