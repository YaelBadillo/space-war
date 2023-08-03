import pyglet
import random
from game import fighter, resources, background

window = pyglet.window.Window(width=1000, height=750)
batch = pyglet.graphics.Batch()

background = background.Background(
    resources.background_image, 100, batch)

fighter = fighter.Fighter(batch=batch,
                          x=window.width / 2, y=(window.height / 2) - 150)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    fighter.on_key_press(symbol, modifiers)


@window.event
def on_key_release(symbol, modifiers):
    fighter.on_key_release(symbol, modifiers)


def update(dt):
    background.update(dt)
    fighter.update(dt)


def generate_asteroids(dt):
    pass


pyglet.clock.schedule_interval(update, 1 / 60.0)

pyglet.clock.schedule_interval(update, 0.5)

if __name__ == '__main__':
    pyglet.app.run()
