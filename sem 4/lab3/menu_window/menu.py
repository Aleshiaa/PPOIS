import pygame
from pygame.locals import *
from checkers.constants import LIGHT_YELLOW, LIGHT_BLUE, FONT, WIDTH, HEIGHT, SQUARE_SIZE, FPS, click_sound, audio_path
from menu_window.help_window import display_help_screen
from checkers.game import Game
from menu_window.settings.settings_window import SettingsWindow
from multiplay_window import MultiplayWindow
from result_window import ResultWindow
from record_table import display_record_table
from result_window_not_players import ResultWindowNotPlayers

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
settings = SettingsWindow(WIN)
multiplay = MultiplayWindow(WIN)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_menu(screen):
    screen.fill(LIGHT_BLUE)

    title_text = FONT.render("Menu", True, LIGHT_YELLOW)
    start_text = FONT.render("Start game", True, LIGHT_YELLOW)
    record_text = FONT.render("Record table", True, LIGHT_YELLOW)
    help_text = FONT.render("Help", True, LIGHT_YELLOW)
    exit_text = FONT.render("Exit", True, LIGHT_YELLOW)
    settings_text = FONT.render("Settings", True, LIGHT_YELLOW)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 280))
    screen.blit(record_text, (WIDTH // 2 - record_text.get_width() // 2, 350))
    screen.blit(help_text, (WIDTH // 2 - help_text.get_width() // 2, 420))
    screen.blit(settings_text, (WIDTH // 2 - settings_text.get_width() // 2, 490))
    screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, 560))


def main_menu():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click_sound.play()
                start_text_width, start_text_height = FONT.size("Start game")
                record_text_width, record_text_height = FONT.size("Record table")
                help_text_width, help_text_height = FONT.size("Help")
                settings_text_width, settings_text_height = FONT.size("Settings")
                exit_text_width, exit_text_height = FONT.size("Exit")

                start_button_y = 280
                record_button_y = 350
                help_button_y = 420
                settings_button_y = 490
                exit_button_y = 560

                start_button_rect = pygame.Rect(
                    (WIDTH // 2 - start_text_width // 2, start_button_y),
                    (start_text_width, start_text_height)
                )
                record_button_rect = pygame.Rect(
                    (WIDTH // 2 - record_text_width // 2, record_button_y),
                    (start_text_width, start_text_height)
                )
                help_button_rect = pygame.Rect(
                    (WIDTH // 2 - help_text_width // 2, help_button_y),
                    (help_text_width, help_text_height)
                )
                settings_button_rect = pygame.Rect(
                    (WIDTH // 2 - settings_text_width // 2, settings_button_y),
                    (settings_text_width, settings_text_height)
                )
                exit_button_rect = pygame.Rect(
                    (WIDTH // 2 - exit_text_width // 2, exit_button_y),
                    (exit_text_width, exit_text_height)
                )

                if start_button_rect.collidepoint(pos):
                    click_sound.play()
                    result = multiplay.run_multiplay()
                    if result == "One player":
                        game_loop(False)
                    elif result == "Two players":
                        game_loop(True)
                    elif result == "Online":
                        continue
                    elif result == "Back":
                        continue
                elif record_button_rect.collidepoint(pos):
                    result = display_record_table()
                    if result == "Back":
                        continue
                elif help_button_rect.collidepoint(pos):
                    click_sound.play()
                    result = display_help_screen(WIN)
                    if result == "Back":
                        continue
                elif settings_button_rect.collidepoint(pos):
                    click_sound.play()
                    result = settings.run_settings()
                    if result == "Back":
                        continue

                elif exit_button_rect.collidepoint(pos):
                    click_sound.play()
                    pygame.quit()
                    exit()

        draw_menu(WIN)
        pygame.display.flip()


def game_loop(is_two_players):
    time = 0
    game = Game(WIN)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play(-1)

    running = True
    while running:
        time = pygame.time.get_ticks()
        if game.winner() is not None:
            print(game.winner())
            if is_two_players:
                result_window = ResultWindow(WIN)
                result_window.run_result(game.winner(), time/1000)
            else:
                result_window = ResultWindowNotPlayers(WIN)
                result_window.run_result(time/1000)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col, is_two_players)
                click_sound.play()


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    settings.settings.toggle_music()
                elif event.key == pygame.K_UP:
                    if settings.settings.volume < 1.0:
                        settings.settings.set_volume(min(settings.settings.volume + 0.1, 1.0))
                elif event.key == pygame.K_DOWN:
                    if settings.settings.volume > 0.0:
                        settings.settings.set_volume(max(settings.settings.volume - 0.1, 0.0))

        game.update()
    pygame.mixer.music.stop()


if __name__ == "__main__":
    main_menu()
