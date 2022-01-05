import pygame

from Screen import Screen

class Stats:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font('assets/DancingScript.ttf', 30)

    def show(self, score, lives):
        score_text = self.font.render(f'Score: {score}', (255, 0, 0), (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (Screen.WIDTH - 150, 10)

        lives_text = self.font.render(f'Lives: {lives}', (255, 0, 0), (255, 255, 255))
        lives_text_rect = lives_text.get_rect()
        lives_text_rect.topleft = (Screen.WIDTH - 150, 60)    

        self.display.blit(score_text, score_text_rect)
        self.display.blit(lives_text, lives_text_rect)        