import pygame
from random import shuffle, randint

TILE = 64
WIN_SIZE = pygame.Rect(0, 0, TILE * 20, TILE * 14)
GAME_SIZE = pygame.Rect(TILE, TILE, TILE * 18, TILE * 12)

BACKGROUND = 'data/back.png'
PLAYER_IDLE = 'data/player.png'
ENEMY_IDLE = 'data/mushroom_idle.png'
ENEMY_DMG = 25
ENEMY_HP = 100
ENEMY_SPEED = 1

HARD_BLOCKS = 'S'
ANIM_SPEED = 32

PLAYER_SIZE = (TILE * 2, TILE * 2)
PLAYER_SPEED = 5
BOMB = 'data/bomb.png'
BULLET = 'data/bullet.png'
STONE = 'data/stone1.png'
CHEST = 'data/chest.png'

BULLET_DIE = 'data/bullet_die.png'
BOSS_BULLET_SPEED = 5
HEAP = ''
BULLET_SPEED = 10
FPS = 120
BOSS_IMAGE = 'data/spider.png'
BULLET_DMG = 25
BOMB_DMG = 50
SPIDER_HP = 100
DOOR_X, DOOR_Y = 0, 0
SPAWN_ROOM = 'rooms/spawn_room.txt'
BOSS_ROOM = 'rooms/boss_room.txt'
# SPAWN_ROOM = BOSS_ROOM

BOSS = {
    'hp': 250,
    'dmg': 12.5,
    'bullet_dmg': 12.5
}

BOOSTS = {
    'heart': [25, 0],
    'key': [0, 0],
    'bomb': [0, 0],
    'coin': [0, 0]
}

LIST = [f'rooms/room{i}.txt' for i in range(5)]
ROOM_LIST, MAPS_SPRITES = [[0 for i in range(3)] for j in range(3)], {}
MAP_IMAGES = [[0 for i in range(3)] for j in range(3)]

LIST.extend([BOSS_ROOM, SPAWN_ROOM])
shuffle(LIST)

for i in LIST:
    x, y = randint(0, 2), randint(0, 2)
    while ROOM_LIST[x][y]:
        x, y = randint(0, 2), randint(0, 2)
    ROOM_LIST[x][y] = i
for i in ROOM_LIST:
    for j in i:
        MAPS_SPRITES[j] = ''
print(ROOM_LIST)
for i in ROOM_LIST:
    for j in i:
        if j != 0:
            if j == 'rooms/spawn_room.txt':
                MAP_IMAGES[ROOM_LIST.index(i)][i.index(j)] = 'data/spawn_room.png'
            elif j == 'rooms/boss_room.txt':
                MAP_IMAGES[ROOM_LIST.index(i)][i.index(j)] = 'data/boss_room.png'
            else:
                MAP_IMAGES[ROOM_LIST.index(i)][i.index(j)] = 'data/room.png'
print(MAP_IMAGES)
