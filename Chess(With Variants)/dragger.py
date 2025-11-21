import pygame
from pygame import Vector2
from const import *

class Dragger:

  def __init__(self):
    self.piece = None
    self.pos = (0,0)
    self.origin = Square(0,0)

  def draw(self,surface):
    if self.piece == None: return
    img = self.piece.image
    self.piece.image_rect = img.get_rect(center=self.pos)
    surface.blit(self.piece.image, self.piece.image_rect)

  def drag(self,piece):
    if piece == None: return
    self.origin = Square(self.pos[0] // SIZE, self.pos[1] // SIZE)
    self.piece = piece