from . import ship, resources


class Fighter(ship.Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(
            img=resources.fighter_image, *args, **kwargs)

        self.velocity_x = 300
        self.velocity_y = 300

    def on_key_press(self, symbol, modifiers):
        self.image = resources.fighter_move_animation
        return super().on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.image = resources.fighter_image
        return super().on_key_release(symbol, modifiers)

    def handle_collides_with(self, other_object):
        if other_object.__class__ is not self.__class__:
            self.image = resources.fighter_destroyed_animation

        return super().handle_collides_with(other_object)
