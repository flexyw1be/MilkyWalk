import pygame
from config import *
from utilities import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((0, 0), PLAYER_SIZE)
        self.image = image_load(PLAYER_IDLE, PLAYER_SIZE)
        self.vx, self.vy = 0, 0

    def upadate(self):
        pass
