import pyglet

from . import image_loader
from utils.center_image import center_image


class AnimationLoader:
    pyglet = pyglet
    loaded_animations = dict()

    @classmethod
    def load(cls, image_path, rows, columns, duration, loop):
        if image_path in cls.loaded_animations:
            return cls.loaded_animations[image_path]

        image = image_loader.ImageLoader.centered_image().load(image_path)

        texture_sequence = cls.pyglet.image.ImageGrid(
            image, rows=rows, columns=columns)
        for texture in texture_sequence:
            center_image(texture)

        animation = cls.pyglet.image.Animation.from_image_sequence(
            texture_sequence, duration=duration, loop=loop)

        cls.loaded_animations[image_path] = animation

        return animation

    @classmethod
    def get_animation(cls, image_path):
        if cls.load[image_path]:
            return cls.loaded_animations[image_path]

        return None

    @classmethod
    def unload(cls, image_path):
        if image_path in cls.loaded_animations:
            del cls.loaded_animations[image_path]

    @classmethod
    def unload_all(cls):
        cls.loaded_animations.clear()
