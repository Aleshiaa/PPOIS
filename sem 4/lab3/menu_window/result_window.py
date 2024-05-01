import pygame
from pygame.locals import *
from checkers.constants import LIGHT_YELLOW, LIGHT_BLUE, FONT, WIDTH, HEIGHT, RESULT_FONT, click_sound, win_sound
from record_table import add_record_to_json


class ResultWindow:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

    def draw_result(self, winner: str, input_str, time):
        self.screen.fill(LIGHT_YELLOW)
        title_text = FONT.render("result", True, LIGHT_BLUE)
        design_text = FONT.render("----------------", True, LIGHT_BLUE)
        winner_text = RESULT_FONT.render(f"{winner} is winner", True, LIGHT_BLUE)
        time_text = RESULT_FONT.render(f"You're time is {time}s", True, LIGHT_BLUE)
        input_text = RESULT_FONT.render("Input name:" + input_str, True, LIGHT_BLUE)
        exit_text = FONT.render("Exit", True, LIGHT_BLUE)
        back_text = FONT.render("Back to menu", True, LIGHT_BLUE)

        pygame.display.flip()

        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        self.screen.blit(design_text, (10, 150))
        self.screen.blit(winner_text, (10, 250))
        self.screen.blit(time_text, (10, 375))
        self.screen.blit(input_text, (10, 500))
        self.screen.blit(exit_text, (300, 600))
        self.screen.blit(back_text, (120, 700))

    def run_result(self, winner: str, time):
        input_str = ""
        running = True
        pygame.mixer.music.stop()
        win_sound.play()
        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    click_sound.play()

                    back_text_width, back_text_height = FONT.size("Back to menu")
                    back_button_rect = pygame.Rect((120, 700), (back_text_width, back_text_height))
                    if back_button_rect.collidepoint(pos):
                        return "Back"
                    exit_text_width, exit_text_height = FONT.size("Exit")
                    exit_button_rect = pygame.Rect((300, 600),(exit_text_width, exit_text_height))
                    if exit_button_rect.collidepoint(pos):
                        click_sound.play()
                        pygame.quit()
                        exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        click_sound.play()
                        add_record_to_json(input_str, time)
                        return "Back"
                    elif event.key == pygame.K_BACKSPACE:
                        click_sound.play()
                        input_str = input_str[:-1]
                    else:
                        click_sound.play()
                        input_str += event.unicode
            self.draw_result(winner, input_str, time)
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Result Window')

    result_window = ResultWindow(screen)
    result_window.run_result("YELLOW", 10.56)
