import pygame
from config import *


def image_load(path, size=(TILE, TILE), alpha=True):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, size)
    if alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image