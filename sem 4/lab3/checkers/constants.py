import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
FPS = 60

# rgb
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (146, 155, 222)
LIGHT_BLUE = (81, 93, 181)
DARK_BLUE = (34, 41, 97)
LIGHT_YELLOW = (217, 187, 104)
WHITE = (240, 226, 189)

# assets
FONT_PATH = os.path.join(os.getcwd(), 'D:/Python-Checkers/assets/fonts/emulogic.ttf')
FONT = pygame.font.Font(FONT_PATH, 48)
HELP_FONT = pygame.font.Font(FONT_PATH, 16)
RESULT_FONT = pygame.font.Font(FONT_PATH, 32)
WHITE_CROWN = pygame.transform.scale(pygame.image.load('D:/Python-Checkers/assets/images/white_crown.png'), (80, 80))
BLACK_CROWN = pygame.transform.scale(pygame.image.load('D:/Python-Checkers/assets/images/black_crown.png'), (80, 80))
WHITE_CHECKER = pygame.transform.scale(pygame.image.load('D:/Python-Checkers/assets/images/white_checkers.png'), (80, 80))
BLACK_CHECKER = pygame.transform.scale(pygame.image.load('D:/Python-Checkers/assets/images/black_checkers.png'), (80, 80))
audio_path = os.path.join(os.getcwd(), 'D:/Python-Checkers/assets/sounds/asoi.mp3')
click_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'D:/Python-Checkers/assets/sounds/cell-click.mp3'))
crown_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'D:/Python-Checkers/assets/sounds/x-click.mp3'))
win_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "D:/Python-Checkers/assets/sounds/win.mp3"))

