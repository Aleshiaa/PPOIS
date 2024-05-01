import pygame


class Settings:
    def __init__(self):
        self.music_on = True
        self.volume = 0.5

    def toggle_music(self):
        self.music_on = not self.music_on
        if self.music_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)
