import pygame

from Ball import Ball
from EndMessage import EndMessage
from Stats import Stats
from Sounds import Sounds

class Game:

    def __init__(self, display):
        self.clock = pygame.time.Clock()
        self.display = display
        self.stats_font = Stats(self.display)
        self.end_font = EndMessage(self.display)
        self.sounds = Sounds()
        self.ball = Ball(self.display)
        self.score = 0
        self.lives = 5
        self.run = True
        self.gameplay = True

    def run_game(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.gameplay and self.ball.collide_point(event.pos):
                        self.score += 1
                        self.ball.bounce()
                        self.sounds.bounce()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p and self.gameplay == False:
                    self.gameplay = True
                    self.score = 0
                    self.lives = 5
                    self.ball = Ball(self.display)

            if self.gameplay and self.ball.collide_borders():
                self.sounds.fail()
                self.lives -= 1    
                        
            self.display.fill((0,128,128))
            self.stats_font.show(self.score, self.lives)

            if self.lives > 0:
                self.ball.move()
                self.ball.show()
            else:
                self.gameplay = False
                self.end_font.show()
            pygame.display.update()

            self.clock.tick(60)        