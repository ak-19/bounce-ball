import pygame

class EndMessage:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font('assets/DancingScript.ttf', 52)

    def show(self):
        text = self.font.render(f'Game over', (255, 0, 0), (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (400, 300)
 
        self.display.blit(text, text_rect)
 