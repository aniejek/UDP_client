import pygame as pg


from game_object import GameObject, Frame


class State(GameObject):
    def __init__(self, width=400, height=300):
        self.objects = []
        self.width = width
        self.height = height
        self.screen = None

    def draw(self):
        for object in self.objects:
            object.draw()

    def update(self, frame: Frame):
        for object, sub_frame in zip(self.objects, frame):
            object.update(sub_frame)

    @classmethod
    def get_initial_state(cls) -> 'State':
        state = cls()
        pg.init()
        state.screen = pg.display.set_mode((state.width, state.height))
        return state

    def add(self, object):
        object.screen = self.screen
        self.objects.append(object)
