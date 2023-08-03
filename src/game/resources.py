import pyglet


def center_image(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


fighter_image = pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/space/Fighter/Idle.png')
# center_image(fighter_image)

fighter_move_image = pyglet.image.load(
    '/home/yxel/Documents/pyglet/space-war/src/assets/space/Fighter/Move.png')
center_image(fighter_move_image)
fighter_move_texture_sequence = pyglet.image.ImageGrid(
    fighter_move_image, rows=1, columns=6)
fighter_move_animation = pyglet.image.Animation.from_image_sequence(
    fighter_move_texture_sequence, duration=0.8, loop=True)
