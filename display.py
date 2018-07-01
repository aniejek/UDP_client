import pygame as pg
from time import clock
from random import randint
from random import random as rand

STEP = 30
FPS = 50  # int(input('podaj ilość klatek na sekundę:\n'))


class Rect:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, x=None, y=None, width=None, height=None, c=None, speed=None, screen=None):
        x = x if x is not None else randint(0, 300)
        y = y if y is not None else randint(0, 100)
        width = width if width is not None else randint(30, 50)
        height = height if height is not None else randint(30, 50)
        c = c if c is not None else (randint(0, 255), randint(0, 255), randint(0, 255))
        speed = speed if speed is not None else 1 + 2 * rand()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.c = c
        self.__speed__ = speed
        self.__screen__ = screen

    def draw(self):
        pg.draw.rect(self.__screen__, self.c, pg.Rect(
            self.x, self.y, self.width, self.height))

    def set_color(self, r, g, b):
        self.c = (r, g, b)

    def set_height(self, height):
        self.height = height

    def set_x(self, x):
        self.x = x

    def get_speed(self):
        return self.__speed__

    def move(self, direction, time):
        scope = time * self.__screen__
        if direction == Rect.UP:
            self.y -= scope
        elif direction == Rect.DOWN:
            self.y += scope
        elif direction == Rect.RIGHT:
            self.x += scope
        elif direction == Rect.LEFT:
            self.x -= scope


class State:
    def __init__(self, width=400, height=300):
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
frame = clock()
i = 0
while not done:
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # key service
    keys = pg.key.get_pressed()
    if keys[pg.K_q]:
        done = True

    # counting time delta
    delta = STEP*(clock() - frame)
    frame = clock()
    v_dir = 0
    h_dir = 0
    # up
    if keys[pg.K_UP]:
        v_dir += -1
    # down
    if keys[pg.K_DOWN]:
        v_dir += 1
    # left
    if keys[pg.K_LEFT]:
        h_dir += -1
    # right
    if keys[pg.K_RIGHT]:
        h_dir += 1

    if (clock() - t) > (1.0 / FPS):
        print(i)
        i = 0
        t += 1.0 / FPS
        state.update(bytes(10))

    pg.display.flip()
