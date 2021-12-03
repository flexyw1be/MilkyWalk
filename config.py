import pygame
from random import shuffle, randint

TILE = 64
WIN_SIZE = pygame.Rect(0, 0, TILE * 20, TILE * 14)
GAME_SIZE = pygame.Rect(TILE, TILE, TILE * 18, TILE * 12)

BACKGROUND = 'data/back.png'
PLAYER_IDLE = 'data/player.png'
ENEMY_IDLE = 'data/spider.png'
ENEMY_DMG = 25
ENEMY_SPEED = 1

HARD_BLOCKS = 'S'

PLAYER_SIZE = (TILE * 2, TILE * 2)
PLAYER_SPEED = 5
BOMB = 'data/bomb.png'
BULLET = 'data/bullet.png'
STONE = 'data/tile_0047.png'
CHEST = 'data/chest.png'
HEAP = ''
BULLET_SPEED = 10
FPS = 120
BULLET_DMG = 50
BOMB_DMG = 50
SPIDER_HP = 100
DOOR_X, DOOR_Y = 0, 0
SPAWN_ROOM = 'rooms/spawn_room.txt'
BOSS_ROOM = 'rooms/boss_room.txt'

BOOSTS = {
    'heart': [25, 0],
    'key': [0, 0],
    'bomb': [0, 0]
}

LIST = [SPAWN_ROOM]
for i in range(6):
    LIST.append(f'rooms/room{i}.txt')
shuffle(LIST)
LIST = LIST[:-2]
LIST.append(BOSS_ROOM)
ROOM_LIST = [[0 for i in range(3)] for j in range(3)]
for i in LIST:
    x, y = randint(0, 2), randint(0, 2)
    while ROOM_LIST[x][y]:
        x, y = randint(0, 2), randint(0, 2)
    ROOM_LIST[x][y] = i
print(ROOM_LIST)
