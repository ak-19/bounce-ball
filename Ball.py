import pygame

from random import randint, choice

class Ball:
    def __init__(self, display):
        self.display = display
        self.image = pygame.image.load('assets/ball.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (randint(10, 750),100)
        self.velocity = 1
        self.dx = choice([self.velocity, -self.velocity])
        self.dy = self.velocity
        self.accel = .25

    def collide_point(self, p):
        return self.rect.collidepoint(p)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def bounce(self):
        self.velocity += self.accel
        self.dx = self.velocity if self.dx > 0 else -self.velocity
        self.dy = self.velocity if self.dy < 0 else -self.velocity

    def collide_borders(self):
        if self.rect.x < 0: self.dx = -self.dx
        if self.rect.y < 0: self.dy = -self.dy
        if self.rect.x + 64 >= 800: self.dx = -self.dx

        if self.rect.y + 64 >= 600: 
            self.dy = -self.dy
            return True
        
        return False

    def show(self):
        self.display.blit(self.image, self.rect)