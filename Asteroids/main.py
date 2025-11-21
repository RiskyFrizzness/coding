from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame.locals import *
from sys import exit
from const import *
from player import Player
from laser import Laser
from asteroid import Asteroid
from math import cos, sin
from time import sleep

playing = True

pygame.init()
pygame.font.init()
font = pygame.font.Font()

screen = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption('Asteroids')
clock = pygame.time.Clock()

player = Player()
lasers = []
asteroids = [Asteroid() for i in range(10)]

pygame.time.set_timer(USEREVENT, 1000)

def main():
  while playing:
    handle_events()  
    update()
    draw()
  game_over()

def handle_events():
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == USEREVENT:
      asteroids.append( Asteroid() )
    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        x_offset = 55 * sin(player.direction)
        y_offset = 55 * cos(player.direction)
        lasers.append(Laser(player, x_offset, y_offset))
        x_offset *= -1
        y_offset *= -1   
        lasers.append(Laser(player, x_offset, y_offset))
      
  keys = pygame.key.get_pressed()
  if keys[K_w]:
    player.thrust()
  if keys[K_a]:
    player.rotate(.075)
  if keys[K_d]:
    player.rotate(-.075)
  if keys[K_UP]:
    player.thrust()
  if keys[K_LEFT]:
    player.rotate(.075)
  if keys[K_RIGHT]:
    player.rotate(-.075)

def update():
  global playing
  player.update()
  for asteroid in asteroids:
    asteroid.update()
    if asteroid.rect.collidepoint(player.x,player.y):
      playing = False
    for laser in lasers:
      if asteroid.rect.collidepoint(laser.x,laser.y):
        asteroids.pop(asteroids.index(asteroid))
        lasers.pop(lasers.index(laser))
        break

  for laser in lasers:
    if laser.update() < 1:
      lasers.pop(0)
  clock.tick(30)


def draw():
  screen.fill((0,0,0))
  for laser in lasers:
    laser.draw(screen)
  for asteroid in asteroids:
    asteroid.draw(screen)
  player.draw(screen)
  pygame.display.flip()
def game_over():
  cat = pygame.image.load("cAt.png")
  cat = pygame.transform.smoothscale_by(cat, 5/7)
  text = font.render("YOU DED", True, (255,0,0))
  rect = cat.get_rect()
  screen.blit(cat,rect)
  rect1 = text.get_rect(center = (500,300))
  screen.blit(text,rect1)
  pygame.display.flip()
  sleep(1)
  
main()
