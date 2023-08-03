import pyglet
import random
from game import ship, resources

window = pyglet.window.Window(width=800, height=600)
batch = pyglet.graphics.Batch()

background_speed = 100

background_image = pyglet.image.load(
    "/home/yxel/Documents/pyglet/space-war/src/assets/background/blue-nebula/blue-nebula-2.png")
background_sprites = [pyglet.sprite.Sprite(
    background_image, batch=batch) for _ in range(2)]
for bg in background_sprites:
    bg.width = window.width

# Posición inicial del primer sprite
background_sprites[0].y = 0

# Posición inicial del segundo sprite, justo encima del primero
background_sprites[1].y = background_sprites[0].height

move_texture_sequence = pyglet.image.ImageGrid(pyglet.image.load(
    "/home/yxel/Documents/pyglet/space-war/src/assets/space/Fighter/Move.png"), rows=1, columns=6)
move_animation = pyglet.image.Animation.from_image_sequence(
    move_texture_sequence, duration=0.2, loop=True)

evasion_texture_sequence = pyglet.image.ImageGrid(pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/space/Fighter/Evasion.png'), rows=1, columns=8)
evasion_animation = pyglet.image.Animation.from_image_sequence(
    evasion_texture_sequence, duration=0.8, loop=True)

x, y = window.width / 2, window.height / 2
speed = 400

# fighter_image = pyglet.image.load(
#    '/home/yxel/Documents/pyglet/space-war/src/assets/space/Fighter/Idle.png')
# fighter = pyglet.sprite.Sprite(img=fighter_image, x=x, y=y, batch=batch)
# fighter.rotation = -90

fighter = ship.Ship(img=resources.fighter_image)

meteor_image = pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/space-objects/PNG/Meteors/Meteor_06.png')
meteor_image.anchor_x = meteor_image.width // 2
meteor_image.anchor_y = meteor_image.height // 2
meteor_sprites = list()

keys = set()


@window.event
def on_draw():
    window.clear()
    batch.draw()
    for meteor_sprite in meteor_sprites:
        meteor_sprite.draw()


@window.event
def on_key_press(symbol, modifiers):
    # fighter.image = move_animation
    fighter.on_key_press(symbol, modifiers)


@window.event
def on_key_release(symbol, modifiers):
    # fighter.image = fighter_image
    fighter.on_key_release(symbol, modifiers)


def create_meteors(dt):
    meteor_sprite = pyglet.sprite.Sprite(img=meteor_image)
    meteor_sprite.scale = 0.2
    meteor_sprite.y = window.height
    meteor_sprite.x = random.randint(0, window.width)
    meteor_sprites.append(meteor_sprite)


def update(dt):
    fighter.update(dt)

    global x, y

    if pyglet.window.key.W in keys:
        y += speed * dt
    if pyglet.window.key.S in keys:
        y -= speed * dt
    if pyglet.window.key.A in keys:
        x -= speed * dt
    if pyglet.window.key.D in keys:
        x += speed * dt

    fighter.x = x
    fighter.y = y

    for sprite in background_sprites:
        sprite.y -= background_speed * dt

        if sprite.y <= -sprite.height:
            sprite.y = background_sprites[0].height

    for meteor_sprite in meteor_sprites:
        meteor_sprite.y -= 500 * dt
        meteor_sprite.rotation += 5


pyglet.clock.schedule_interval(create_meteors, 1 / 2)


pyglet.clock.schedule_interval(update, 1 / 60.0)

if __name__ == "__main__":
    pyglet.app.run()
