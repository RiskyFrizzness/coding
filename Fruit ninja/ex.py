import pygame


class X:
    image = [pygame.image.load(f'x{i}.png') for i in range(4)]
    def __init__(self):
        self.value = 0
    
    def draw(self,screen):
        screen.blit(X.image[self.value],X.image[self.value].get_rect(topright=(1150,50)))