import socket
import pygame as pg

from math import cos, sin, pi
# from matplotlib import pyplot as plt
from time import clock, sleep
# from random import randint
# from random import random as rand

STEP = 30
FPS = 50  # int(input('podaj liczbe klatek na sekundę:\n'))
ONE_FRAME_TIME = 1 / 50
SWIDTH = 800
SHEIGHT = 600
RWIDTH = 100
RHEIGHT = 100
TANK_R = 60
BULLET_R = 10
GUN_R = 20
GUN_POS = TANK_R - GUN_R
DEGRIES = 720
FULL_CIRCLE = 360
DEGRIES_TO_RADIANS = 2 * pi / FULL_CIRCLE
DEGREE = FULL_CIRCLE / DEGRIES
OBJECT_BYTE_SIZE = 14

coss = []
sins = []

for degree in [i * DEGREE for i in range(DEGRIES)]:
    coss.append(cos(degree * DEGRIES_TO_RADIANS))
    sins.append(sin(degree * DEGRIES_TO_RADIANS))


def gun_cords(x, y, axis):
    gun_x = GUN_POS * coss[axis]
    gun_y = GUN_POS * sins[axis]
    return int(x - gun_x), int(y - gun_y)


def draw_tank(x, y, axis, c, cg, surface):
    pg.draw.circle(surface, c, (x, y), TANK_R)
    gun_x, gun_y = gun_cords(x, y, axis)
    pg.draw.circle(surface, cg, (gun_x, gun_y), GUN_R)


# class Rect:
#     UP = 0
#     DOWN = 1
#     LEFT = 2
#     RIGHT = 3
#
#     def __init__(self, x=None, y=None, width=None, height=None, c=None, speed=None, screen=None):
#         x = x if x is not None else randint(0, 300)
#         y = y if y is not None else randint(0, 100)
#         width = width if width is not None else randint(30, 50)
#         height = height if height is not None else randint(30, 50)
#         c = c if c is not None else (randint(0, 255), randint(0, 255), randint(0, 255))
#         speed = speed if speed is not None else 1 + 2 * rand()
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.c = c
#         self.__speed__ = speed
#         self.__screen__ = screen
#
#     def draw(self):
#         pg.draw.rect(self.__screen__, self.c, pg.Rect(
#             self.x, self.y, self.width, self.height))
#
#     def set_color(self, r, g, b):
#         self.c = (r, g, b)
#
#     def set_height(self, height):
#         self.height = height
#
#     def set_x(self, x):
#         self.x = x
#
#     def get_speed(self):
#         return self.__speed__
#
#     def move(self, direction, time):
#         scope = time * self.__screen__
#         if direction == Rect.UP:
#             self.y -= scope
#         elif direction == Rect.DOWN:
#             self.y += scope
#         elif direction == Rect.RIGHT:
#             self.x += scope
#         elif direction == Rect.LEFT:
#             self.x -= scope
#


class State:
    def __init__(self, width=SWIDTH, height=SHEIGHT):
        self.objects = []
        self.width = width
        self.height = height
        self.screen = None

    def update(self, frame: bytes):
        for object, byte in zip(self.objects, frame):
            object.update(byte)

    @classmethod
    def get_initial_state(cls) -> 'State':
        state = cls()
        pg.init()
        state.screen = pg.display.set_mode((state.width, state.height))
        return state

    def add(self, object):
        object.screen = self.screen
        self.objects.append(object)


v_dir = 0
h_dir = 0
state = State.get_initial_state()
done = False
t = clock()
i = 0
UDP_IP_F = "192.168.0.192"
UDP_IP_T = "192.168.0.241"
UDP_PORT_F = 5005
UDP_PORT_T = 9876
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP_F, UDP_PORT_F))
frame = clock()
elo = []
while not done:

    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # key service
    keys = pg.key.get_pressed()
    if keys[pg.K_q]:
        done = True

    data, address = sock.recvfrom(1024)
    state.screen.fill((0, 0, 0))
    b = 0
    while b < len(data):
        obj_data = data[b:b+OBJECT_BYTE_SIZE]
        b += OBJECT_BYTE_SIZE
        x = int.from_bytes(obj_data[:4], 'big')
        y = int.from_bytes(obj_data[4:8], 'big')
        axis = int.from_bytes(obj_data[8:12], 'big')
        # elo.append(axis)
        obj_type = int.from_bytes(obj_data[12:], 'big')
        if obj_type == 257:
            draw_tank(x, y, axis, (200, 100, 50), (50, 200, 100), state.screen)
        else:
            pg.draw.circle(state.screen, (50, 100, 200), (x, y), BULLET_R)




    # if x < 0:
    #     x = 0
    # if y < 0:
    #     y = 0
    # if x > SWIDTH - RWIDTH:
    #     x = SWIDTH - RWIDTH
    # if y > SHEIGHT - RHEIGHT:
    #     y = SHEIGHT - RHEIGHT
    # pg.draw.rect(state.screen, (100, 100, 100), pg.Rect(x, y, RWIDTH, RHEIGHT))



    #

    # counting time delta
    # delta = STEP*(clock() - frame)
    # frame = clock()
    # v_dir = 0
    # h_dir = 0
    # up
    res = 0

    if keys[pg.K_RIGHT]:
        res += 4

    if keys[pg.K_LEFT]:
        res += 2
    res *= 2

    if keys[pg.K_DOWN]:
        res += 2
    res *= 2

    if keys[pg.K_UP]:
        res += 2
    res *= 2

    if keys[pg.K_SPACE]:
        res += 2

    res += 1

    # down
    # left
    # right

    # if (clock() - t) > (1.0 / FPS):
    #     print(i)
    #     i = 0
    #     t += 1.0 / FPS
        # state.update(bytes(10))

    sock.sendto(bytes([100, res]), (UDP_IP_T, UDP_PORT_T))
    pg.display.flip()
    # frame_time = clock() - frame
    # if frame_time < ONE_FRAME_TIME:
    #     sleep(ONE_FRAME_TIME - frame_time)
    # frame = clock()
print('xDD')
# plt.plot(range(len(elo)), elo)
# plt.show()
# wait = True
# while wait:
#     for event in pg.event.get():
#         if event.type == pg.KEYDOWN:
#             wait = False
# pass
