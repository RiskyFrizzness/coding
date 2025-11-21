import pygame
from os import listdir
from collections import namedtuple

WIDTH = 600
SIZE = WIDTH//8
COLOR1 = (234,235,200)
COLOR2 = (119,154,88)
M_LIGHT = (200,100,100)
M_DARK = (200,72,72)
L_LIGHT = (172,195,51)
L_DARK = (244,247,116)
Square = namedtuple('Square', 'col row')
Move = namedtuple('Move', 'origin target')
D_OUTLINE = (0,0,0)
L_OUTLINE = (255,255,255)
# board colors change on turn

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
UP_LEFT = (-1,-1)
UP_RIGHT = (1,-1)
DOWN_LEFT = (-1,1)
DOWN_RIGHT = (1,1)

def loadgraphics():
  global graphics
  graphics = {}
  names = [i for i in listdir('graphics')]
  for name in names:
    image = pygame.image.load(f'graphics/{name}').convert_alpha()
    image = pygame.transform.smoothscale(image, (SIZE,SIZE))
    graphics[name[:-4]] = image