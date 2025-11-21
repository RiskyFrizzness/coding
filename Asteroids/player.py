import pygame
from const import *
from math import sin, cos, pi, degrees

x_wing = pygame.image.load("Player.png")
x_wing = pygame.transform.smoothscale_by(x_wing,0.1)
x_wing = pygame.transform.rotate(x_wing,-90)

class Player:
  def __init__(self):
    self.direction = pi / 2
    self.image = x_wing
    self.image = pygame.transform.rotate(x_wing,degrees(self.direction))
    self.x = WIDTH//2
    self.y = WIDTH//2
    self.x_velocity = 0
    self.y_velocity = 0
  
  def rotate(self, angle):
    self.direction += angle 
    self.image = pygame.transform.rotate(x_wing,degrees(self.direction))
  
  def thrust(self):
    aceleration = .25
    self.x_velocity += aceleration * cos(self.direction)
    self.y_velocity += aceleration * -sin(self.direction)
  
  def update(self):
    self.x += self.x_velocity
    self.y += self.y_velocity
    self.x %= WIDTH
    self.y %= WIDTH

  def draw(self, screen):
    rect = self.image.get_rect(center = (self.x,self.y))
    screen.blit(self.image, rect)