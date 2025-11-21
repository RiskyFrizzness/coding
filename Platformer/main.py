from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame.locals import *
from sys import exit
from player import Player
from level import Level
from level import maps

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

player = Player()
level = 0

GREEN = pygame.Color(13,255,0,255)
RED = pygame.Color(237,28,36,255)
GREY = pygame.Color(70,70,70,255)
YELLOW = pygame.Color(255,0,255,255)

def main():
    while True:
        clock.tick(FPS)
        handle_events()
        update()
        draw()

def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

def update():
    global player, level
    player.dx = 7
    handle_collision()
    if player.update(maps[level]):
        level += 1
        player = Player()

def handle_collision():
    global level
    for tile in maps[level]:
        if tile.rect.colliderect(player.rect):
            if tile.color == GREEN:
                player.dy *= 0.4
                player.dx = 3
            if tile.color == YELLOW:
                level += 1




def draw():
    screen.fill((100,100,100))
    maps[level].draw(screen)
    player.draw(screen)
    pygame.display.flip()

main()