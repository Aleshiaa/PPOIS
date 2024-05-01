from .constants import LIGHT_BLUE, SQUARE_SIZE, BLACK_CROWN, WHITE_CROWN, BLACK_CHECKER, WHITE_CHECKER, crown_sound
import pygame


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color, black):
        self.row = row
        self.col = col
        self.color = color
        self.black = black
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
        crown_sound.play()

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, LIGHT_BLUE, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.black:
            if self.king:
                win.blit(BLACK_CROWN, (self.x - BLACK_CROWN.get_width() // 2, self.y - BLACK_CROWN.get_height() // 2))
            else:
                win.blit(BLACK_CHECKER, (self.x - BLACK_CHECKER.get_width() // 2, self.y - BLACK_CHECKER.get_height() // 2))
        else:
            if self.king:
                win.blit(WHITE_CROWN, (self.x - WHITE_CROWN.get_width() // 2, self.y - WHITE_CROWN.get_height() // 2))
            else:
                win.blit(WHITE_CHECKER, (self.x - WHITE_CHECKER.get_width() // 2, self.y - WHITE_CHECKER.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
