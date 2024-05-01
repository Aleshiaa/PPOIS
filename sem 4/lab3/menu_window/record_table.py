import pygame
from pygame.locals import *
from checkers.constants import LIGHT_YELLOW, LIGHT_BLUE, WIDTH, HEIGHT, FONT, HELP_FONT
import json


def draw_record_table(screen):
    screen.fill(LIGHT_YELLOW)

    title_text = FONT.render("Records", True, LIGHT_BLUE)
    back_text = FONT.render("Back to menu", True, LIGHT_BLUE)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
    screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 150))
    with open('records.json', 'r') as file:
        records = json.load(file)
    sorted_records = sorted(records.items(), key=lambda x: x[1], reverse=False)
    top_records = sorted_records[:10]

    y_offset = 150
    for idx, (player, time) in enumerate(top_records):
        player_text = HELP_FONT.render(f"{idx+1}. {player}:", True, LIGHT_BLUE)
        time_text = HELP_FONT.render(f"{time} seconds", True, LIGHT_BLUE)

        screen.blit(player_text, (100, y_offset + idx * 50))
        screen.blit(time_text, (500, y_offset + idx * 50))


def display_record_table():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Records')

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

                back_text_width, back_text_height = FONT.size("Back to menu")
                back_button_rect = pygame.Rect(
                    (WIDTH // 2 - back_text_width // 2, HEIGHT - 150),
                    (back_text_width, back_text_height)
                )

                if back_button_rect.collidepoint(pos):
                    return "Back"

        draw_record_table(screen)
        pygame.display.flip()

    pygame.quit()


def add_record_to_json(input_str, time):
    with open('records.json', 'r') as file:
        records = json.load(file)
    records[input_str] = time
    with open('records.json', 'w') as file:
        json.dump(records, file)


if __name__ == "__main__":
    display_record_table()
