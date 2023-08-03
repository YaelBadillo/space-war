from pyglet.window import key
from . import physicalobject


class Ship(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Ship, self).__init__(*args, **kwargs)

        self.rotation = -90
        self.velocity_x = 300
        self.velocity_y = 300

        self.keys = dict(up=False, down=False, left=False, right=False)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            self.keys['up'] = True
        if symbol == key.S:
            self.keys['down'] = True
        if symbol == key.A:
            self.keys['left'] = True
        if symbol == key.D:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.W:
            self.keys['up'] = False
        if symbol == key.S:
            self.keys['down'] = False
        if symbol == key.A:
            self.keys['left'] = False
        if symbol == key.D:
            self.keys['right'] = False

    def update(self, dt):
        if self.keys['up']:
            self.y += self.velocity_y * dt
        if self.keys['down']:
            self.y -= self.velocity_y * dt
        if self.keys['left']:
            self.x -= self.velocity_x * dt
        if self.keys['right']:
            self.x += self.velocity_x * dt
