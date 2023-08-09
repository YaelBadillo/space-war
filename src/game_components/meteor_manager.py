import random

from game_objects import meteor
from resources import image_loader


class MeteorManager:
    def __init__(self, window_width, window_height, batch):
        self.__window_width = window_width
        self.__window_height = window_height
        self.__batch = batch
        self.__meteors = list()

    def generate_meteors(self, dt):
        meteor_instance = meteor.Meteor(difficulty=1, img=image_loader.ImageLoader.centered_image(
        ).load('assets/space-objects/PNG/Meteors/Meteor_05.png'), batch=self.__batch)
        meteor_instance.x = random.randint(
            0 + meteor_instance.width / 2, self.__window_width - meteor_instance.width / 2)
        meteor_instance.y = self.__window_height + meteor_instance.image.width / 2
        self.__meteors.append(meteor_instance)

    def update(self, dt):
        for meteor in self.__meteors:
            meteor.update(dt)

        self.__remove_out_meteors()

    def __remove_out_meteors(self):
        for meteor in self.__meteors:
            if meteor.y < -meteor.height:
                self.__meteors.remove(meteor)

    def get_meteors(self):
        return self.__meteors
