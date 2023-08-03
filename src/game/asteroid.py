from . import physicalobject, resources


class Asteroid(physicalobject):
    def __init__(self, difficulty, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._difficulty = difficulty
        self._speed = 150 * self._difficulty

    def update(self, dt):
        self.y -= self._speed * dt
