from const import *
import pygame
from board import Board
from dragger import Dragger
from piece import *
import tkinter as tk

class Game:
  
  def __init__(self, game_type='Normal'):
    self.game_type = game_type
    self.board = Board()
    self.dragger = Dragger()
    self.turn = 'white'
    self.show_moves = True

  def draw_bg(self,surface):
    for row in range(8):
      for col in range(8):
        if (row + col) % 2 == 0:
          color = (COLOR2)# light green
        else:
          color = (COLOR1)# dark green
            
        rect = (col * SIZE, row * SIZE, SIZE, SIZE)
        pygame.draw.rect(surface,color,rect)
  def on_mouse_motion(self,pos):
    self.hover_square = Square(pos[0] // SIZE, pos[1 // SIZE])
    self.dragger.pos = pos
  def on_mouse_down(self,pos):
    col = pos[0] // SIZE
    row = pos[1] // SIZE
    piece = self.board[col][row]
    if not piece: return
    if piece.color != self.turn: return
    piece.update_moves(Square(col,row), self.board)
    self.dragger.pos = pos
    self.dragger.drag(piece)
    
  def on_mouse_up(self,pos):
    col = pos[0] // SIZE
    row = pos[1] // SIZE
    move = Move(self.dragger.origin, Square(col,row))
    nuke = False
    if self.dragger.piece:
      if move in self.dragger.piece.moves:

        nuke = bool(self.board[col][row])     
        if type(self.dragger.piece) == Pawn and move.target:
          pass
        if type(self.dragger.piece) == Pawn and (move.target[1] == 0 or move.target[1] == 7):
          self.promote()   
        self.board.move(self.dragger.piece, move) 
        self.next_turn()
    self.dragger.piece = None
    if nuke and self.game_type=='Atomic':
      for i in range(col-1,col+2):
        for j in range(row-1,row+2):
          if i not in range(0,8): continue
          if j not in range(0,8): continue
          if type(self.board[i][j]) == Pawn and self.board[i][j] is not self.dragger.piece: continue
          self.board[i][j] = None
      self.board[col][row] = None
    
  def draw(self,surface):
    self.draw_bg(surface)
    self.draw_last_move(surface)
    if self.show_moves:
      self.draw_moves(surface)
      self.draw_last_move(surface)
    self.draw_outline(surface)
    self.board.draw(surface, self.dragger.piece)
    self.dragger.draw(surface)
    
  def draw_outline(self, surface):
    color = D_OUTLINE if self.turn == 'black' else L_OUTLINE
    rect = (0,0,WIDTH,WIDTH)
    pygame.draw.rect(surface,color,rect,5)
    

  
  def draw_moves(self,surface):
    if not self.dragger.piece: return
    piece = self.dragger.piece
    for move in piece.moves:
      if (move.target.col + move.target.row) % 2 == 0:
        color = M_LIGHT
      else:
        color = M_DARK
      rect = (move.target.col * SIZE, move.target.row * SIZE, SIZE, SIZE)
      pygame.draw.rect(surface, color, rect)

  def draw_last_move(self,surface):
    if not self.board.last_move: return
    for square in self.board.last_move:
      if (square.col + square.row) % 2 == 0:
        color = L_LIGHT
      else:
        color = L_DARK
      rect = (square.col * SIZE, square.row * SIZE, SIZE, SIZE)
      pygame.draw.rect(surface, color, rect)

  def toggle_highlight(self):
    if self.show_moves == True: self.show_moves = False
    elif self.show_moves == False: self.show_moves = True

  def next_turn(self):
    if self.turn == 'white':
      self.turn = 'black'
    else:
      self.turn = 'white'

  def promote(self):
    root = tk.Tk()
    root.geometry("125x75")
    stringvar = tk.StringVar(root)
    stringvar.set("Queen")
    optionmenu = tk.OptionMenu(root, stringvar, "Queen", "Bishop", "Knight","Rook").pack()
    tk.Button(root, text="Submit", command=root.destroy).pack()
    tk.mainloop()
    self.dragger.piece = {"Queen":Queen, "Bishop":Bishop, "Knight":Knight, "Rook":Rook}[stringvar.get()](self.dragger.piece.color)

