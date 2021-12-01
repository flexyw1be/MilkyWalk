import pygame
from random import shuffle, randint

TILE = 64
WIN_SIZE = pygame.Rect(0, 0, TILE * 20, TILE * 14)
GAME_SIZE = pygame.Rect(TILE, TILE, TILE * 18, TILE * 12)

BACKGROUND = 'data/back.png'
PLAYER_IDLE = 'data/1.jpg'
ENEMY_IDLE = 'data/sider.png'
ENEMY_DMG = 25
ENEMY_SPEED = 0.2
PLAYER_SIZE = (128, 128)
PLAYER_SPEED = 5
BOMB = 'data/bomb.png'
BULLET = 'data/bullet.png'
STONE = 'data/tile_0047.png'
CHEST = ''
HEAP = ''
BULLET_SPEED = 8
FPS = 120
BULLET_DMG = 15
BOMB_DMG = 50
DOOR_X, DOOR_Y = 0, 0
SPAWN_ROOM = 'rooms/spawn_room.txt'
BOSS_ROOM = 'rooms/boss_room.txt'
LIST = [SPAWN_ROOM]
for i in range(6):
    LIST.append(f'rooms/room{i}.txt')
shuffle(LIST)
LIST = LIST[:-2]
LIST.append(BOSS_ROOM)
ROOM_LIST = [[0 for i in range(3)] for j in range(3)]
print(ROOM_LIST)
for i in LIST:
    x, y = randint(0, 2), randint(0, 2)
    while ROOM_LIST[x][y]:
        x, y = randint(0, 2), randint(0, 2)
    ROOM_LIST[x][y] = i



