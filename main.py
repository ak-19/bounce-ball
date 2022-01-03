import pygame

from Ball import Ball
from Stats import Stats

pygame.init()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Bounce the ball')

bounce_sound = pygame.mixer.Sound('assets/bounce.wav')

stats_font = Stats(display)

ball = Ball(display)

score = 0
lives = 5

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if ball.collide_point(event.pos):
                score += 1
                bounce_sound.play()
                
    display.fill((0,128,128))
    stats_font.show(score, lives)
    ball.show()
    pygame.display.update()

pygame.quit()