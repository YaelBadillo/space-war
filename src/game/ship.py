from pyglet.window import key
from . import physical_object


class Ship(physical_object.PhysicalObject):
    def __init__(self, img, *args, **kwargs):
        super(Ship, self).__init__(img=img, *args, **kwargs)

        self.img = img
        self.rotation = -90
        self.velocity_x = 200
        self.velocity_y = 200
        self.scale = 0.8

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

        self.__check_bounds()

    def __check_bounds(self):
        min_x = -self.img.width / 2
        min_y = -self.img.height / 2
        max_x = 1000 + self.img.width / 2
        max_y = 750 + self.img.height / 2
        if self.x < min_x:
            self.x = max_x
        if self.y < min_y:
            self.y = max_y
        if self.x > max_x:
            self.x = min_x
        if self.y > max_y:
            self.y = min_y
