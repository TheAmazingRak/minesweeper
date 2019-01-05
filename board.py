from field import Field
import random
import sys


class Board:
    fields = [[]]
    screen = None
    assets = None
    font = None
    width = 0
    height = 0
    margin = margin_x, margin_y = 0, 0

    def __init__(self, screen):
        self.screen = screen

    def create_board(self, w, h):
        self.width = w
        self.height = h
        self.fields = [[None for i in range(self.height)] for j in range(self.width)]

        for x in range(self.width):
            for y in range(self.height):
                f = Field(self.screen)
                f.font = self.font
                f.set_text("")

                f.set_image(self.assets.get_image("field"))

                if random.randint(0, 9) > 8:
                    f.is_mine = True

                self.fields[x][y] = f

    def draw_board(self):
        for x in range(self.width):
            for y in range(self.height):
                f = self.fields[x][y]
                
                f.draw(f.width * x + self.margin_x, 
                       f.height * y + self.margin_y)

    def on_click(self, mouse_btn, x, y):
        # get clicked field
        x, y = self.world_to_cell(x - self.margin_x, 
                                  y - self.margin_y)
        f = self.fields[x][y]

        # left click
        if mouse_btn == 1:
            # if field is flagged prevent from showing it, 
            # 'cause u know, it can be a bomb
            if f.is_flagged:
                pass

            # if clicked field is a bomb,
            # kermit suicide
            elif f.is_mine:
                self.kermit_suicide()

            # show field
            else:
                self.get_mines_count(x, y)

                if f.mines_around == 0:
                    self.uncover_empty_fields(x, y)
                else:
                    f.show = True

                f.set_image(self.assets.get_image("uField"))

                if f.mines_around != 0:
                    f.set_text(f.mines_around)

                print(f.mines_around)
        
        # right click
        elif mouse_btn == 3:
            # if field is not showed (which means it has no number, it's uncovered),
            # place flag on that field if it's not already placed or remove flag if it is
            if not f.show:
                if f.is_flagged:
                    f.is_flagged = False
                    f.set_image(self.assets.get_image("field"))
                else:
                    f.is_flagged = True
                    f.set_image(self.assets.get_image("flag"))

        # middle / wheel click
        elif mouse_btn == 2:
            pass

    def get_fields_around(self, x, y):
        fields = []

        for _x in range(-1, 2):
            for _y in range(-1, 2):
                if x - _x < 0 or y - _y < 0:
                    continue

                if _x == 0 and _y == 0:
                    continue

                try:
                    f = self.fields[x - _x][y - _y]
                except IndexError:
                    continue
                else:
                    fields.append(f)
        
        return fields

    def get_mines_count(self, x, y):
        f = self.fields[x][y]
        f.mines_around = 0

        for field in self.get_fields_around(x, y):
            if field.is_mine:
                f.mines_around += 1

    def uncover_empty_fields(self, x, y):
        self.get_mines_count(x, y)
        f = self.fields[x][y]

        if not f.show and not f.is_flagged:
            f.show = True
            f.set_image(self.assets.get_image("uField"))

            if f.mines_around == 0:

                if x > 0:
                    self.uncover_empty_fields(x - 1, y)

                if x < len(self.fields[y]) - 1:
                    self.uncover_empty_fields(x + 1, y)

                if y > 0:
                    self.uncover_empty_fields(x, y - 1)

                if y < len(self.fields) - 1:
                    self.uncover_empty_fields(x, y + 1)

            else:
                f.set_text(f.mines_around)

    def kermit_suicide(self):
        self.show_all()

    def show_all(self):
        for x in range(self.width):
            for y in range(self.height):
                f = self.fields[x][y]

                f.show = True

                if f.is_mine:
                    f.set_image(self.assets.get_image("bomb"))
                else:
                    self.get_mines_count(x, y)

                    if f.mines_around != 0:
                        f.set_text(f.mines_around)

    def world_to_cell(self, x, y):
        return (int(x / self.fields[0][0].width),
                int(y / self.fields[0][0].height))

    def cell_to_world(self, x, y):
        return (x * self.fields[0][0].width, 
                y * self.fields[0][0].height)
                    