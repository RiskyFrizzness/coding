import pygame
from pygame import Rect, Color
from random import randint

class Brick():

    def __init__(self, pos):
        self.rect = Rect(pos, (35,15))
        self.color = Color(255,0,0,0)
        self.color.hsla = (randint(0, 360),*self.color.hsla[1:])

    def update(self):
        pass

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect,3)
