import pygame
from pygame import Rect, Vector2
from random import choice, randint, uniform

class Fruit:
    kinds = ("apple","watermelon", "orange", "peach","coconut","pear","bomb")
    images = [pygame.image.load(f'{name}.png') for name in kinds]
    images[-1] = pygame.transform.smoothscale_by(images[-1],0.1)
    for i in range(len(images)):
        images[i] = pygame.transform.smoothscale_by(images[i],1.8)

    def __init__(self):
        self.kind = randint(0,len(Fruit.kinds)-1)
        self.image = Fruit.images[self.kind]
        self.pos = Vector2(randint(0,1200),820)
        self.velocity = Vector2(self.pos.x,-uniform(12.6,17))
        self.velocity.x = uniform(self.pos.x /-171,(1200-self.pos.x)/171)
        self.angle: float = 0.0
        self.angular_velocity: float = uniform(-4,4)

    def update(self):
        self.pos += self.velocity
        self.velocity += Vector2(0,.2)
        self.image = pygame.transform.rotate(Fruit.images[self.kind], self.angle)
        self.angle += self.angular_velocity
        mouse_pos = Vector2(pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[0] and self.pos.distance_to(mouse_pos) < 25:
            return True
        return False

    def draw(self, screen:pygame.Surface):
        screen.blit(self.image,self.image.get_rect(center=self.pos))

class Slice:
    images = [[pygame.transform.smoothscale_by(pygame.image.load(f'{name}{i}.png'),1.8)for i in range(2)] for name in Fruit.kinds[:-1]]
    def __init__(self, fruit:Fruit, variant:int):
        self.image = Slice.images[fruit.kind][variant]
        self.kind: int = fruit.kind
        self.variant: int = variant
        self.pos: Vector2 = fruit.pos.copy()
        self.angle: float = fruit.angle
        self.angular_velocity: float = fruit.angular_velocity
        self.velocity: Vector2 = fruit.velocity.copy().rotate(uniform(-90,90))

    def update(self):
        self.pos += self.velocity
        self.velocity += Vector2(0,.2)
        self.image = pygame.transform.rotate(Slice.images[self.kind][self.variant], self.angle)
        self.angle += self.angular_velocity

    def draw(self, screen:pygame.Surface):
        screen.blit(self.image,self.image.get_rect(center=self.pos))
        