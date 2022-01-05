import pygame

class EndMessage:
    def __init__(self, display):
        self.display = display
        self.main_font = pygame.font.Font('assets/DancingScript.ttf', 52)
        self.helper_font = pygame.font.Font('assets/DancingScript.ttf', 34)

    def show(self):
        game_over = self.main_font.render(f'Game over', (255, 0, 0), (255, 255, 255))
        game_over_rect = game_over.get_rect()
        game_over_rect.center = (400, 300)

        instructions_text = self.helper_font.render(f'Press "p" to play again', (255, 0, 0), (255, 255, 255))
        instructions_text_rect = instructions_text.get_rect()
        instructions_text_rect.center = (400, 400)

        self.display.blit(game_over, game_over_rect)
        self.display.blit(instructions_text, instructions_text_rect)
 