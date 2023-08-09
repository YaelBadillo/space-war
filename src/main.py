import pyglet
from game import background, meteor_manager
from game_objects.ships import fighter
from resources import image_loader

window = pyglet.window.Window(width=1000, height=750)
batch = pyglet.graphics.Batch()

background = background.Background(image_loader.ImageLoader.load(
    'assets/background/purple-nebula/purple-nebula-7.png'), 100, batch)

fighter = fighter.Fighter(batch=batch,
                          x=window.width / 2, y=(window.height / 2) - 150)

meteor_manager = meteor_manager.MeteorManager(
    window_width=window.width, window_height=window.height, batch=batch)


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
    meteor_manager.update(dt)

    meteors = meteor_manager.get_meteors()
    if not fighter.is_dead:
        for meteor in meteors:
            is_collide = fighter.collides_with(meteor)
            if is_collide:
                fighter.handle_collides_with(meteor)


pyglet.clock.schedule_interval(update, 1 / 60.0)

pyglet.clock.schedule_interval(meteor_manager.generate_meteors, 0.5)

if __name__ == '__main__':
    pyglet.app.run()
