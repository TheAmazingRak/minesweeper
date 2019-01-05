import pygame
import sys
from assets import Assets
from board import Board
from color import Color

# init
pygame.init()
pygame.display.set_caption("Minesweeper")

size = width, height = 900, 600
screen = pygame.display.set_mode(size)

# load assets
assets = Assets()

# font
arial = pygame.font.SysFont("Arial", 30)

# gameboard
board = Board(screen)
board.assets = assets
board.font = pygame.font.SysFont("Arial", 26)
board.margin_x = 0
board.margin_y = 60

# play time counter
counter = 0
counter_m = 0
counter_text = "00:00"
counter_start = False
clock = pygame.time.Clock()


def start():
    board.create_board(15, 15)
    pygame.time.set_timer(pygame.USEREVENT, 1000)


def update():
    global counter
    global counter_m
    global counter_text
    global counter_start
    global board

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                counter_start = True

                pos = pygame.mouse.get_pos()
                board.on_click(event.button, pos[0], pos[1])

            # counter
            if counter_start:
                if event.type == pygame.USEREVENT:
                    if counter == 59:
                        counter_m += 1
                        counter = 0
                    else:
                        counter += 1

                    if counter_m < 10:
                        counter_text = "0" + str(counter_m) + ":"
                    else:
                        counter_text = str(counter_m) + ":"

                    if counter < 10:
                        counter_text += "0" + str(counter)
                    else:
                        counter_text += str(counter)

        screen.fill(Color.Black)

        # gameobject draw
        board.draw_board()
        screen.blit(arial.render(counter_text, False, Color.White), (5, 10))
        
        pygame.display.flip()


if __name__ == "__main__":
    start()
    update()
