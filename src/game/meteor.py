from . import physicalobject, resources


class Meteor(physicalobject.PhysicalObject):
    def __init__(self, difficulty, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._difficulty = difficulty
        self._speed = 150 * self._difficulty
        self.rotation = 90

        self.scale = 0.3

    def update(self, dt):
        self.y -= self._speed * dt
