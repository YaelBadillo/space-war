import pyglet


def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


# Background image
background_image = pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/background/purple-nebula/purple-nebula-7.png')

# Fighter image
fighter_image = pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/space/Fighter/Idle.png')
center_image(fighter_image)

# Fighter move image
fighter_move_image = pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/space/Fighter/Move.png')
# Fighter move image splitted into several images
fighter_move_texture_sequence = pyglet.image.ImageGrid(
    fighter_move_image, rows=1, columns=6)
for img in fighter_move_texture_sequence:
    center_image(img)
# Fighter move animation
fighter_move_animation = pyglet.image.Animation.from_image_sequence(
    fighter_move_texture_sequence, duration=0.8, loop=True)

# Fighter destroyed image
fighter_destroyed_image = pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/space/Fighter/Destroyed.png')
fighter_destroyed_texture_sequence = pyglet.image.ImageGrid(
    fighter_destroyed_image, rows=1, columns=15)
for img in fighter_destroyed_texture_sequence:
    center_image(img)

fighter_destroyed_animation = pyglet.image.Animation.from_image_sequence(
    fighter_destroyed_texture_sequence, duration=0.1, loop=False)

meteor_image = pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/space-objects/PNG/Meteors/Meteor_05.png')
center_image(meteor_image)
