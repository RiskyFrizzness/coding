from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from const import *
from game import Game
import pygame, sys
from pygame.locals import *
import tkinter as tk

#https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces
print('"c" is to turn of highlight')

class Main:

  def __init__(self):
    pygame.init() 
    self.screen = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption("Chess")
    loadgraphics()
    from const import graphics
    pygame.display.set_icon(graphics['black_rook'])
    self.game = Game(self.choose_type())

  def choose_type(self):
    root = tk.Tk()
    root.geometry("200x100")
    v = tk.StringVar(root, "Normal")
    values = {"Standard" : "Normal","Atomic" : "Atomic",}
    for (text, value) in values.items(): 
      tk.Radiobutton(root, text = text, variable = v, value = value).pack(side = tk.TOP, ipady = 5)
    tk.Button(root, text="Sumbit", command=root.destroy).pack()
    tk.mainloop()
    return v.get()
 

  def mainloop(self):
    dragger = self.game.dragger
    while True:
      for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN:
          self.game.on_mouse_down(event.pos)

        elif event.type == MOUSEMOTION:
          self.game.on_mouse_motion(event.pos)

        elif event.type == MOUSEBUTTONUP:
          self.game.on_mouse_up(event.pos)

        if event.type == KEYDOWN:
          if event.key == K_c:
            self.game.toggle_highlight()

          
        if event.type == QUIT:
          return
      self.game.draw(self.screen)
      pygame.display.update()

main = Main()
main.mainloop()