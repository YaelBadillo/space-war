import pyglet


class BackgroundManager():
    __number_of_sprites = 2

    def __init__(self, background_image, speed, batch):
        self.__background_sprites = [pyglet.sprite.Sprite(
            background_image, batch=batch) for _ in range(BackgroundManager.__number_of_sprites)]

        self.__speed = speed

        self.__set_background_sprites_position()

    def __set_background_sprites_position(self):
        self.__background_sprites[0].y = 0
        self.__background_sprites[1].y = self.__background_sprites[0].height

    def update(self, dt):
        for background_sprite in self.__background_sprites:
            background_sprite.y -= self.__speed * dt

            if background_sprite.y <= -background_sprite.height:
                background_sprite.y = self.__background_sprites[0].height
