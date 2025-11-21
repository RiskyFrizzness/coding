from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from brick import Brick
from ball import Ball
from paddle import Paddle
from pygame import Surface, Vector2
from pygame.time import Clock
from pygame.event import Event
from pygame.locals import QUIT
from sys import exit

pygame.init()
FPS: int = 60
screen: Surface = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Breakout")
clock: Clock = Clock()
pygame.mouse.set_visible(False)

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
    return events

def update(events: list[Event]) -> None:
    paddle.update()
    ball.update()
    if paddle.rect.colliderect(ball.rect):
        ball.velocity.reflect_ip(Vector2(0,1))
        ball.velocity.y = -25
        ball.velocity += Vector2((ball.center.x-paddle.rect.centerx)*0.1,0)
        ball.center.y = paddle.rect.top - ball.RADIUS
    for brick in bricks:
        if ball.rect.colliderect(brick.rect):#if brick.rect.colliderect(brick.rect): #better code        
           ball.collide_brick(brick.rect)
           bricks.remove(brick)
           break
           

def draw() -> None:
    screen.fill('black')
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)
    pygame.display.flip()

bricks = []
for y in range(100,300,15):
    for x in range(150,1000,35):
        bricks.append(Brick((x,y)))

paddle = Paddle()
ball = Ball()

main()