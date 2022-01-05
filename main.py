import pygame

from Ball import Ball
from EndMessage import EndMessage
from Stats import Stats

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Bounce the ball')

bounce_sound = pygame.mixer.Sound('assets/bounce.wav')
fail_sound = pygame.mixer.Sound('assets/fail.wav')

stats_font = Stats(display)
end_font = EndMessage(display)


ball = Ball(display)

score = 0
lives = 5


run = True
gameplay = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if gameplay and ball.collide_point(event.pos):
                score += 1
                ball.bounce()
                bounce_sound.play()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p and gameplay == False:
            gameplay = True
            score = 0
            lives = 5
            ball = Ball(display)

    if gameplay and ball.collide_borders():
        fail_sound.play()
        lives -= 1    
                
    display.fill((0,128,128))
    stats_font.show(score, lives)

    if lives > 0:
        ball.move()
        ball.show()
    else:
        gameplay = False
        end_font.show()
    pygame.display.update()

    clock.tick(60)

pygame.quit()