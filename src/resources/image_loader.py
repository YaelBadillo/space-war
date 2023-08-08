import pyglet

from utils.center_image import center_image


class ImageLoader:
    pyglet = pyglet
    loaded_images = dict()
    center = False

    @classmethod
    def load(cls, image_path):
        if image_path in cls.loaded_images:
            return cls.loaded_images[image_path]

        if cls.center:
            image = cls.pyglet.image.load(image_path)
            center_image(image)
            cls.center = False
        else:
            image = cls.pyglet.image.load(image_path)

        cls.loaded_images[image_path] = image

        return image

    @classmethod
    def centered_image(cls):
        cls.center = True
        return cls

    @classmethod
    def get_image(cls, image_path):
        if cls.load[image_path]:
            return cls.loaded_images[image_path]

        return None

    @classmethod
    def unload(cls, image_path):
        if image_path in cls.loaded_images:
            del cls.loaded_images[image_path]

    @classmethod
    def unload_all(cls):
        cls.loaded_images.clear()
