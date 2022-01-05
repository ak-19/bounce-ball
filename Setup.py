import pygame

from Screen import Screen

class Setup:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Bounce the ball')
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        
    def get_display(self):
        return pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

    def quit(self):
        pygame.quit()
