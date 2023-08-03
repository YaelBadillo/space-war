from pyglet.window import key
from . import physicalobject


class Ship(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Ship, self).__init__(*args, **kwargs)

        self.rotation = 90

        self.keys = dict(up=False, down=False, left=False, right=False)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.keys['up'] = True
        if symbol == key.S:
            self.keys['down'] = True
        if symbol == key.A:
            self.keys['left'] = True
        if symbol == key.A:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.A:
            self.keys['up'] = False
        if symbol == key.S:
            self.keys['down'] = False
        if symbol == key.A:
            self.keys['left'] = False
        if symbol == key.A:
            self.keys['right'] = False
