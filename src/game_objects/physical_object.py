from abc import ABC, abstractclassmethod

import pyglet


class PhysicalObject(ABC, pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.is_dead = False

    @abstractclassmethod
    def update(self, dt):
        pass

    def collides_with(self, other_object) -> bool:
        return (self.x < other_object.x + other_object.width and
                self.x + self.width / 2 > other_object.x and
                self.y < other_object.y + other_object.height and
                self.y + self.height / 2 > other_object.y)

    def handle_collides_with(self, other_object):
        if other_object.__class__ is not self.__class__:
            self.is_dead = True
