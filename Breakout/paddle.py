import pygame
from pygame import Rect
from pygame.math import clamp

class Paddle():
    def __init__(self):
        self.rect = Rect(0,700,100,15)

    def update(self):
        self.rect.centerx = clamp(pygame.mouse.get_pos()[0],self.rect.w//2,1200-self.rect.w//2)

    def draw(self,screen):
        pygame.draw.rect(screen,'white',self.rect)
