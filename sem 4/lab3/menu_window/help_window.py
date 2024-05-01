import pygame
from pygame.locals import *
from checkers.constants import LIGHT_YELLOW, LIGHT_BLUE, WIDTH, HEIGHT, FONT, HELP_FONT, click_sound


def read_help_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def render_paragraphs(screen, text, font, color, x, y, max_width):
    words = [word.split(' ') for word in text.splitlines()]
    space_width, line_height = font.size(' ')[0], font.size(text)[1]
    current_x, current_y = x, y

    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()

            if current_x + word_width >= x + max_width:
                current_x = x
                current_y += line_height

            screen.blit(word_surface, (current_x, current_y))
            current_x += word_width + space_width
        current_x = x
        current_y += line_height


def draw_help(screen):
    screen.fill(LIGHT_YELLOW)

    help_title_text = FONT.render("Help", True, LIGHT_BLUE)
    back_text = FONT.render("Back to menu", True, LIGHT_BLUE)

    screen.blit(help_title_text, (WIDTH // 2 - help_title_text.get_width() // 2, 50))
    screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 150))

    help_content = read_help_text('help.txt')
    max_width = 750
    render_paragraphs(screen, help_content, HELP_FONT, LIGHT_BLUE, WIDTH // 2 - max_width // 2, 150, max_width)


def display_help_screen(screen):
    pygame.init()

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click_sound.play()

                back_text_width, back_text_height = FONT.size("Back to menu")
                back_button_rect = pygame.Rect(
                    (WIDTH // 2 - back_text_width // 2, HEIGHT - 150),
                    (back_text_width, back_text_height)
                )

                if back_button_rect.collidepoint(pos):
                    return "Back"

        draw_help(screen)
        pygame.display.flip()

    pygame.quit()
