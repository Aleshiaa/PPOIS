import pygame
from pygame.locals import *
from checkers.constants import LIGHT_YELLOW, LIGHT_BLUE, FONT, WIDTH, HEIGHT, click_sound


class MultiplayWindow:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

    def draw_multiplay(self):
        self.screen.fill(LIGHT_YELLOW)

        title_text = FONT.render("choose mode", True, LIGHT_BLUE)
        design_text = FONT.render("----------------", True, LIGHT_BLUE)
        player_text = FONT.render("one player", True, LIGHT_BLUE)
        two_player_text = FONT.render("two players", True, LIGHT_BLUE)
        online_text = FONT.render("online", True, LIGHT_BLUE)
        back_text = FONT.render("Back to menu", True, LIGHT_BLUE)

        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        self.screen.blit(design_text, (10, 150))
        self.screen.blit(player_text, (100, 300))
        self.screen.blit(two_player_text, (100, 400))
        self.screen.blit(online_text, (100, 500))
        self.screen.blit(back_text, (100, 700))

    def run_multiplay(self):
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
                    back_button_rect = pygame.Rect((100, 700), (back_text_width, back_text_height))
                    if back_button_rect.collidepoint(pos):
                        return "Back"
                    player_text_width, player_text_height = FONT.size("one player")
                    player_text_rect = pygame.Rect((100, 300), (player_text_width, player_text_height))
                    if player_text_rect.collidepoint(pos):
                        return "One player"
                    two_player_text_width, two_player_text_height = FONT.size("two players")
                    two_player_text_rect = pygame.Rect((100, 400), (two_player_text_width, two_player_text_height))
                    if two_player_text_rect.collidepoint(pos):
                        return "Two players"
                    online_text_width, online_text_height = FONT.size("online")
                    online_text_rect = pygame.Rect((100, 500), (online_text_width, online_text_height))
                    if online_text_rect.collidepoint(pos):
                        return "Online"

            self.draw_multiplay()
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Choose_Mode')

    multiplay_window = MultiplayWindow(screen)
    multiplay_window.run_multiplay()
