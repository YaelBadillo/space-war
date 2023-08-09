from . import ship
from resources import image_loader, animation_loader


class Fighter(ship.Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(img=image_loader.ImageLoader.centered_image().load(
            'assets/space/Fighter/Idle.png'), *args, **kwargs)

        self.velocity_x = 300
        self.velocity_y = 300

    def on_key_press(self, symbol, modifiers):
        self.image = animation_loader.AnimationLoader.load(
            'assets/space/Fighter/Move.png', rows=1, columns=6, duration=0.8, loop=True)
        return super().on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.image = image_loader.ImageLoader.centered_image().load(
            'assets/space/Fighter/Idle.png')
        return super().on_key_release(symbol, modifiers)

    def handle_collides_with(self, other_object):
        if other_object.__class__ is not self.__class__:
            self.image = animation_loader.AnimationLoader.load(
                'assets/space/Fighter/Destroyed.png', rows=1, columns=15, duration=0.1, loop=False)

        return super().handle_collides_with(other_object)
