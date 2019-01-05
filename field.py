import pygame
from color import Color


class Field:
    is_mine = False
    is_flagged = False
    mines_around = 0
    show = False

    screen = None
    image = None
    rect = None
    scale = width, height = 32, 32

    font = None
    text = None
    text_rect = None

    def __init__(self, scr):
        self.screen = scr

    def set_image(self, img):
        self.image = img
        self.image = pygame.transform.scale(self.image, (self.scale[0], self.scale[1]))
        self.rect = self.image.get_rect()

    def set_text(self, mines_around):
        c = Color.Black
        
        if mines_around == 1:
            c = Color.Blue
        elif mines_around == 2:
            c = Color.Green
        elif mines_around == 3:
            c = Color.Red
        elif mines_around == 4:
            c = Color.DarkBlue
        elif mines_around == 5:
            c = Color.Brown

        self.text = self.font.render(str(mines_around), False, c)

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y

        self.text_rect = self.text.get_rect(center=(x + self.width / 2, y + self.height / 2))

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)
