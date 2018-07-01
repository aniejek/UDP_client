from random import randint, random as rand

import pygame as pg

from game_object import GameObject, Frame


class Rect(GameObject):
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

    def update(self, frame: Frame):
        pass

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
