import pygame


class Assets:
    assetsDir = "./Assets/"
    texturesDir = assetsDir + "Textures/"
    fontsDir = assetsDir + "Fonts/"

    textures = {
        "field": pygame.image.load(texturesDir + "field.png"),
        "uField": pygame.image.load(texturesDir + "field_uncovered.png"),
        "bomb": pygame.image.load(texturesDir + "bomb.png"),
        "flag": pygame.image.load(texturesDir + "flag.png"),
    }

    def get_image(self, name):
        return self.textures[name]