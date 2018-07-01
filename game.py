from time import clock

import pygame as pg

from game_object import GameObject, Frame
from display.state import State


class Game(GameObject):
    FPS = 50
    STEP = 30

    def __init__(self):
        self.state = State.get_initial_state()
        pass

    def run(self):
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
            delta = Game.STEP * (clock() - frame)
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

            if (clock() - t) > (1.0 / Game.FPS):
                print(i)
                i = 0
                t += 1.0 / Game.FPS

            pg.display.flip()


