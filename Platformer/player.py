import pygame
from pygame.locals import *

GREEN = pygame.Color(13,255,0,255)
RED = pygame.Color(237,28,36,255)
GREY = pygame.Color(70,70,70,255)
YELLOW = pygame.Color(255,255,0,255)

class Player:
    def __init__(self):
        self.walking = [pygame.image.load(f'assets/walk_{i}.png') for i in range(1,9)]
        self.diving = pygame.image.load('assets/Diving.png').convert_alpha()
        self.idle = pygame.image.load('assets/idle.png')
        self.idle.convert_alpha()
        self.image = self.idle
        self.walking_index = -1
        self.rect = self.image.get_rect(center=(100,600))
        self.dy = 0
        self.face_right = True

    def update(self, level):
        colors = []
        def is_colliding():
            answer = False
            for tile in level:
                if tile.rect.colliderect(self.rect):
                    if tile.color != GREEN:
                        colors.append(tile.color)
                        answer = True
                    if tile.color == RED:
                        self.__init__()
                    
            return answer
        self.dy += 1

        self.rect.y += self.dy
        grounded = False

        if is_colliding():
            self.rect.y -= self.dy
            self.dy = 0 
            grounded = True

        keys = pygame.key.get_pressed()
        idle = True

        if keys[K_a]:
            self.rect.x -= self.dx
            if is_colliding():
                self.rect.x += self.dx
            self.face_right = False
            idle = False

        if keys[K_d]:
            self.rect.x += self.dx
            if is_colliding():
                self.rect.x -= self.dx
            self.face_right = True
            idle = False

        if keys[K_SPACE] and grounded:
            self.dy = -25 if GREY in colors else -13
            idle = False

        if idle:
            self.image = self.idle
        else:
            self.walking_index += 1
            self.walking_index %= len(self.walking)
            self.image = self.walking[self.walking_index]

        if not grounded:
            self.image = self.diving

        if not self.face_right:
            self.image = pygame.transform.flip(self.image,True,False)


        self.image.set_colorkey((89,253,66))
        return YELLOW in colors

    def draw(self, screen):
        screen.blit(self.image, self.rect)