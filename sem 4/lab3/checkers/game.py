import pygame
from .constants import DARK_BLUE, LIGHT_YELLOW, BLUE, SQUARE_SIZE
from checkers.board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.start_time = None
        self.count = 0

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        if self.selected:
            self.draw_selection_circle(self.selected)
        pygame.display.update()

    def draw_selection_circle(self, piece):
        pygame.draw.circle(self.win, (255, 255, 255), (piece.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                            piece.row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2, width=2)

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = DARK_BLUE
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col, is_two_players):
        if self.selected:
            result = self._move(row, col, is_two_players)
            if not result:
                self.selected = None
                self.select(row, col, is_two_players)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            if is_two_players and self.count % 2 == 1:
                self.valid_moves = self.board.get_valid_rotated_moves(piece)
            else:
                self.valid_moves = self.board.get_valid_moves(piece)

            return True

        return False

    def _move(self, row, col, is_two_players):
        if not self.selected:
            return False

        piece = self.board.get_piece(row, col)
        if piece != 0 or (row, col) not in self.valid_moves:
            return False

        start_row, start_col = self.selected.row, self.selected.col
        target_row, target_col = row, col

        dx = (target_col - start_col) * SQUARE_SIZE
        dy = (target_row - start_row) * SQUARE_SIZE


        animation_frames = 30
        clock = pygame.time.Clock()

        for frame in range(1, animation_frames + 1):
            self.selected.x = start_col * SQUARE_SIZE + dx * frame / animation_frames + 50
            self.selected.y = start_row * SQUARE_SIZE + dy * frame / animation_frames + 50

            self.board.draw(self.win)

            pygame.display.update()
            clock.tick(30)

        self.board.move(self.selected, row, col)
        skipped = self.valid_moves.get((row, col))
        if skipped:
            self.board.remove(skipped)

        self.change_turn(is_two_players)
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2,
                                                row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self, is_two_players):
        self.valid_moves = {}
        if self.turn == DARK_BLUE:
            self.turn = LIGHT_YELLOW
            if is_two_players:
                self.board.rotate_board_180()
        else:
            self.turn = DARK_BLUE
            if is_two_players:
                self.board.rotate_board_180()
        self.count+=1
        print(self.count)
