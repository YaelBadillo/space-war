import pyglet
import random
from game import ship, resources

window = pyglet.window.Window(width=800, height=600)
batch = pyglet.graphics.Batch()

fighter = ship.Ship(img=resources.fighter_image, batch=batch,
                    x=window.width / 2, y=window.height / 2)

@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    # fighter.on_key_press(symbol, modifiers)
    pass


@window.event
def on_key_release(symbol, modifiers):
    # fighter.on_key_release(symbol, modifiers)
    pass


def update(dt):
    pass


pyglet.clock.schedule_interval(update, 1 / 60.0)

if __name__ == "__main__":
    pyglet.app.run()
