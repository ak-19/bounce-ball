import pygame

class Ball:
    def __init__(self, display):
        self.display = display
        self.image = pygame.image.load('assets/ball.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (100,100)

    def collide_point(self, p):
        return self.rect.collidepoint(p)

    def show(self):
        self.display.blit(self.image, self.rect)