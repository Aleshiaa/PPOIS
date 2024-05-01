import pygame
from pygame.locals import *
from checkers.constants import LIGHT_YELLOW, LIGHT_BLUE, FONT, WIDTH, HEIGHT, click_sound
from menu_window.settings.settings import Settings


class SettingsWindow:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.settings = Settings()

    def draw_settings(self):
        self.screen.fill(LIGHT_BLUE)

        title_text = FONT.render("Settings", True, LIGHT_YELLOW)
        music_text = FONT.render("----------------", True, LIGHT_YELLOW)
        volume_text = FONT.render(f"Volume: {self.settings.volume:.1f}", True, LIGHT_YELLOW)
        up_symbol = FONT.render("+", True, LIGHT_YELLOW)
        down_symbol = FONT.render("-", True, LIGHT_YELLOW)
        back_text = FONT.render("Back to menu", True, LIGHT_YELLOW)

        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        self.screen.blit(music_text, (10, 150))
        self.screen.blit(volume_text, (100, 400))
        self.screen.blit(up_symbol, (440, 400))
        self.screen.blit(down_symbol, (630, 400))
        self.screen.blit(back_text, (100, 600))

    def run_settings(self):
        running = True
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
                    back_button_rect = pygame.Rect((100, 600), (back_text_width, back_text_height))
                    if back_button_rect.collidepoint(pos):
                        return "Back"
                    up_symbol_width, up_symbol_height = FONT.size("+")
                    up_symbol_rect = pygame.Rect((440, 400), (up_symbol_width, up_symbol_height))
                    if up_symbol_rect.collidepoint(pos):
                        if self.settings.volume < 1.0:
                            self.settings.set_volume(min(self.settings.volume + 0.1, 1.0))
                    down_symbol_width, down_symbol_height = FONT.size("+")
                    down_symbol_rect = pygame.Rect((630, 400), (down_symbol_width, down_symbol_height))
                    if down_symbol_rect.collidepoint(pos):
                        if self.settings.volume > 0.0:
                            self.settings.set_volume(max(self.settings.volume - 0.1, 0.0))
            self.draw_settings()
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Settings')

    settings_window = SettingsWindow(screen)
    settings_window.run_settings()
