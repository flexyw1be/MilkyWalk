import pygame
from utilities import *
from buff import Buff


class Block(pygame.sprite.Sprite):
    def __init__(self, img, coord, size=(TILE, TILE), name='stone'):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load(img, size)
        self.name = name
        self.x, self.y = coord
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.hp = 50

    def update(self, player, buffs):
        if pygame.sprite.collide_rect(self, player) and player.get_keys():
            buff = Buff(self.rect.centerx, self.rect.centery)
            buffs.add(buff)
            self.kill()
            player.set_keys(int(player.get_keys() - 1))

        if self.get_hp() < 1:
            if self.name == 'chest':
                buff = Buff(self.rect.centerx, self.rect.centery)
                buffs.add(buff)

            self.kill()

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp
