import pygame
from math import sin, cos, asin, acos, degrees
from const import *

image = pygame.image.load("Laser.png")

class Laser:
  def __init__(self, player, x_offset, y_offset):
    self.image = pygame.transform.rotate(image,degrees(direction)+90)
    self.x = player.x + x_offset
    self.y = player.y + y_offset
    self.life = FPS * 2
    speed = player.x_velocity ** 2 + player.y_velocity ** 2
    speed **= 0.5
    self.x_velocity = speed * cos(player.direction)
    self.y_velocity = speed * -sin(player.direction)
    self.mask = pygame.mask.from_surface(self.image)

  def update(self):
    self.x += self.x_velocity
    self.y += self.y_velocity
    self.x %= WIDTH
    self.y %= WIDTH
    self.life -= 1
    return self.life
  
  def draw(self, screen):
    rect = self.image.get_rect(center = (self.x,self.y))
    screen.blit(self.image, rect)
    