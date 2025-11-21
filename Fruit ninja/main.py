from os import environ
from random import randint
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.event import Event
from pygame.locals import QUIT, USEREVENT
from sword import Sword
from fruit import Fruit,Slice
from ex import X
from sys import exit

pygame.init()
FPS: int = 60
bg = pygame.transform.smoothscale(pygame.image.load("background.png"),(1200,800))
screen: Surface = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Fruit ninja")
clock: Clock = Clock()

SPAWN = USEREVENT + 1
pygame.time.set_timer(SPAWN, 1000, 1)

def main() -> None:
    while True:
        clock.tick(FPS)
        update(handle_events())
        draw()

def handle_events() -> list[Event]:
    events: list[Event] = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == SPAWN:
            fruits.append(Fruit())
            pygame.time.set_timer(SPAWN, randint(1, 2000), 1)

    return events

def update(events: list[Event]) -> None:
    sword.update()
    for fruit in fruits:
        if fruit.update():
            fruits.remove(fruit)
            if fruit.kind != len(Fruit.kinds)-1:
                slices.extend([Slice(fruit,0), Slice(fruit,1)])
            else:
                x.value +=1
        elif fruit.pos.y > 800 and fruit.velocity.y > 0 and fruit.kind != len(Fruit.kinds)-1:
            fruits.remove(fruit)
            x.value +=1
    for slice in slices:
        slice.update()
        if slice.pos.y > 800:
            slices.remove(slice)


def draw() -> None:
    screen.blit(bg, (0,0))
    x.draw(screen)
    for fruit in fruits:
       fruit.draw(screen)
    for slice in slices:
        slice.draw(screen)
    sword.draw(screen)
    pygame.display.flip()

sword = Sword()
fruits = [Fruit()] 
slices = []
x = X()   
main()