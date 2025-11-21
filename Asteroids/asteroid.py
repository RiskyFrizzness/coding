import pygame
from const import *
from random import randint
from math import cos, sin

img = pygame.image.load("Asteroid.png")
img = pygame.transform.smoothscale_by(img,.3)

class Asteroid:
  def __init__(self):
    self.rect = img.get_rect()
    self.rect.x = randint(0,WIDTH)
    self.rect.y = randint(0,WIDTH)
    if randint(0,1):
      self.rect.x = WIDTH * randint(0,1)
    else:
      self.rect.y = WIDTH * randint(0,1)
    speed = 1
    self.rect.center = (self.rect.x,self.rect.y)
    self.x_velocity = randint(-1,1)
    self.y_velocity = randint(-1,1)
    self.mask = pygame.mask.from_surface(img)

  def update(self):
    self.rect.x += self.x_velocity
    self.rect.y += self.y_velocity
    self.rect.x %= WIDTH
    self.rect.y %= WIDTH
    
  def draw(self, screen):
    screen.blit(img, self.rect)