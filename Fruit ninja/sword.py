import pygame

class Sword:
    sizes = [1,2,3,4,6,4,2,1]
    def __init__(self):
        self.points: list[tuple[int,int]] = []

    def update(self):
        if not pygame.mouse.get_pressed()[0]:
            if self.points:
                self.points.pop(0)
            return
        self.points.append(pygame.mouse.get_pos())
        if len(self.points) > 9:
            self.points.pop(0)

    def draw(self, screen):
        if len(self.points) < 2:
            return
        for i, (a,b) in enumerate(zip(self.points[:-1], self.points[1:])):
            pygame.draw.line(screen, (210,210,210), a,b, Sword.sizes[i])
