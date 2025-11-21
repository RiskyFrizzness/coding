import pygame
from pygame import Rect, Color
from dataclasses import dataclass

@dataclass
class Tile:
    rect: Rect
    color: Color

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Level:
    def __init__(self, surface):
        self.tiles = []
        for x in range(surface.get_width()):
            for y in range(surface.get_height()):
                color = surface.get_at((x,y))
                if color == Color(0,0,0,0):continue             
                self.tiles.append(Tile(Rect(x*20, y*20, 20, 20),color))

    def draw(self,screen):
        for tile in self.tiles:
            tile.draw(screen)

    def __getitem__(self, index):
        return self.tiles[index]
    
maps = [Level(pygame.image.load(f'assets/Map{i+1}.png')) for i in range(3)]
    