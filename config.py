import pygame

TILE = 64
WIN_SIZE = pygame.Rect(0, 0, TILE * 20, TILE * 14)
GAME_SIZE = pygame.Rect(TILE, TILE, TILE * 18, TILE * 12)

BACKGROUND = 'data/back.png'
PLAYER_IDLE = 'data/1.png'
PLAYER_SIZE = (128, 128)
PLAYER_SPEED = 3
BOMB = 'data/bomb1.png'
BULLET = 'data/bullet.png'
STONE = 'data/tile_0047.png'
BULLET_SPEED = 4
FPS = 180
DOOR_X, DOOR_Y = 0, 0
SPAWN_MAP = 'rooms/spawn_map.txt'
BOSS_ROOM = 'rooms/boss_room.txt'
