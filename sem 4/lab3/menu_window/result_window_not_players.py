import pygame
from pygame.locals import *
from checkers.constants import LIGHT_YELLOW, LIGHT_BLUE, FONT, WIDTH, HEIGHT, RESULT_FONT, click_sound, win_sound


class ResultWindowNotPlayers():
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

    def draw_result(self, time):
        self.screen.fill(LIGHT_YELLOW)
        title_text = FONT.render("result", True, LIGHT_BLUE)
        design_text = FONT.render("----------------", True, LIGHT_BLUE)
        time_text = RESULT_FONT.render(f"You're time is {time}s", True, LIGHT_BLUE)
        exit_text = FONT.render("Exit", True, LIGHT_BLUE)
        back_text = FONT.render("Back to menu", True, LIGHT_BLUE)

        pygame.display.flip()

        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        self.screen.blit(design_text, (10, 150))
        self.screen.blit(time_text, (20, 400))
        self.screen.blit(exit_text, (300, 600))
        self.screen.blit(back_text, (120, 700))

    def run_result(self, time):
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
            self.draw_result(time)
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Result Window')

    result_window = ResultWindowNotPlayers(screen)
    result_window.run_result(10.56)
