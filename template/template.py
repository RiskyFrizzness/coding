from sys import path
path.append(r'\\192.168.0.105\Local Shared Folder\Code Coaches\Jordan Newberry\template')
from jordan import Game, on
import pygame

class Videogame(Game):
    caption = 'Videogame'
    def __init__(self):
        Game.__init__(self)

    def update(self):
        pass

    def draw(self):
        self.screen.fill('white')

        pygame.display.update()

if __name__ == '__main__':
    Videogame().loop()