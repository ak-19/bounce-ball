import pygame

class Sounds:        
    def __init__(self):
        pygame.mixer.music.load('assets/spinning.mp3')
        pygame.mixer.music.play(loops=-1)
        self.bounce_sound = pygame.mixer.Sound('assets/bounce.wav')
        self.fail_sound = pygame.mixer.Sound('assets/fail.wav')

    def bounce(self):
        self.bounce_sound.play()
        
    def fail(self):
        self.fail_sound.play()        