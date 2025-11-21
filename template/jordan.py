import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame import display, time
from abc import ABC, abstractmethod
from typing import Callable, Sequence

__all__ = ['Game', 'on', 'load_images'] # only these objects are imported from wildcard

pygame.init()

Coordinate = tuple[float, float] | Sequence[float] | pygame.Vector2

def on(event:int) -> Callable:
    'Marks a method as an event handler'
    def decorator(fn):
        fn._event = event
        return fn
    return decorator

class Game(ABC):
    caption = 'Videogame'
    size: Coordinate = pygame.Vector2(1200, 800)
    fps: int = 60
    flags:int = 0

    def __init__(self) -> None:
        self.screen: pygame.Surface = display.set_mode(self.size, self.flags)
        self.clock: time.Clock = time.Clock()
        self.active: bool = True
        'the game will loop end when this is set to False'
        self._handler_registry: dict[int, Callable] = {
            eh._event:eh for name in dir(self) if hasattr(eh:=getattr(self, name), '_event')
        }
        'event type : event handler'
        display.set_caption(self.caption)

    @abstractmethod
    def update(self) -> None: pass
    @abstractmethod
    def draw(self) -> None: pass

    def loop(self) -> None:
        self.active = True
        while self.active:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

    def handle_events(self) -> None:
        'calls appropriate event handlers decorated with @on'
        for ev in pygame.event.get():
            self._handler_registry.get(ev.type, lambda *_: None)(ev)

    @on(pygame.QUIT)
    def on_quit(self, _) -> None:
        self.active = False

    def __str__(self) -> str:
        return self.__class__.__name__

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} active={self.active} at {id(self):#x}>"


def load_images(directory:str) -> dict[str, pygame.Surface]:
    '''Loads all png, jpg, jpeg, bmp, and gif files '''
    surfaces: dict[str, pygame.Surface] = {}
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    for filename in os.listdir(directory):
        path: str = os.path.join(directory, filename)
        if not os.path.isfile(path): continue
        name, extension = os.path.splitext(filename)
        if not extension.lower() in _extensions: continue
        try:
            surfaces[name] = pygame.image.load(path).convert_alpha()
        except pygame.error as e:
            print(f"Failed to load {path}: {e}")
    return surfaces 

_extensions: frozenset[str] = frozenset({
    '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.xpm' '.lbm', '.pbm',
    '.pgm', '.ppm', '.pcx', '.pnm', '.svg', '.tga', '.tiff', '.tif'
})

if __name__ == "__main__":
    class Empty(Game):
        update = lambda self: None
        draw = lambda self: None
    Empty().loop()