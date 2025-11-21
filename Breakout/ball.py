import pygame
from pygame import Rect, Vector2
from math import pi

class Ball():
    RADIUS = 10*pi / 4
    def __init__(self):
        self.rect = Rect(600,400,20,20)
        self.velocity = Vector2(0,0)
        self.center = Vector2(self.rect.center)

    def update(self):
        self.center += self.velocity
        if self.center.y > 800- Ball.RADIUS or self.center.y < 0+ Ball.RADIUS:
            self.velocity.reflect_ip(Vector2(0,1))
            self.center.y = pygame.math.clamp(self.center.y,0+Ball.RADIUS,800-Ball.RADIUS)
        if self.center.x > 1200- Ball.RADIUS or self.center.x < 0+ Ball.RADIUS:
            self.velocity.reflect_ip(Vector2(1,0))
            self.center.x = pygame.math.clamp(self.center.x, 0+Ball.RADIUS, 1200-Ball.RADIUS)
        self.velocity.y += 0.5
        self.rect.center = self.center 


    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.rect.center,Ball.RADIUS)

    def collide_brick(self,brick:Rect):
        # diff1 = Vector2(brick.centerx-5*10**0.5,brick.centery) - self.center
        # diff2 = Vector2(brick.centerx+5*10**0.5,brick.centery) - self.center
        # normal = diff1 if diff1.magnitude() < diff2.magnitude() else diff2
        # self.velocity.reflect_ip(normal)
        clip = self.rect.clip(brick)
        if clip.w > clip.h:
            self.velocity.reflect_ip(Vector2(0,1))
        else:
            self.velocity.reflect_ip(Vector2(1,0))