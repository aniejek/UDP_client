import pygame as pg
from time import clock
from random import randint

STEP = 30
FPS = 50  # int(input('podaj ilość klatek na sekundę:\n'))


class Rect:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, x, y, w, h, c, s, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.__speed__ = speed
        self.__screen__ = screen

    def draw(self):
        pg.draw.rect(screen, self.c, pg.Rect(
            self.x, self.y, self.w, self.h))

    def set_color(self, r, g, b):
        self.c = (r, g, b)

    def set_height(self, h):
        self.h = h

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


pg.init()
_list = []
screen = pg.display.set_mode((400, 300))
# for i in range(randint(5, 10)):
x = randint(0, 300)
y = randint(0, 100)
w = randint(30, 50)
h = randint(30, 50)
c = (randint(0, 255), randint(0, 255), randint(0, 255))
speed = 2#00.0 / randint(100, 500)
my_rect = Rect(x, y, w, h, c, speed, screen)
_list.append(my_rect)
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

    # up
    if keys[pg.K_UP]:
        my_rect.y -= delta * my_rect.get_speed()
    # down
    if keys[pg.K_DOWN]:
        my_rect.y += delta * my_rect.get_speed()
    # left
    if keys[pg.K_LEFT]:
        my_rect.x -= delta * my_rect.get_speed()
    # right
    if keys[pg.K_RIGHT]:
        my_rect.x += delta * my_rect.get_speed()

    if (clock() - t) > (1.0 / FPS):
        print(i)
        i = 0
        t += 1.0 / FPS
        screen.fill((0, 0, 0))
        for rect in _list:
            rect.draw()

    pg.display.flip()
