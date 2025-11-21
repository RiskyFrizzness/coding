from piece import *

class Board():
  def __init__(self):
    self.last_move = None
    self.board = [[None for i in range(8)] for i in range(8)]
    self.addPieces('white')
    self.addPieces('black')
    
  def __getitem__(self, i):
    return self.board[i]
  
  def draw(self, surface, cpiece):
    for col in range(8):
      for row in range(8):
        if not self.board[col][row]: continue
        piece = self.board[col][row]
        #if piece is self.dragger.piece: continue
        if piece is cpiece: continue
        piece.draw(Square(col,row), surface)
  
  def addPieces(self,color):
    row_capital = 0 if color == 'black' else 7
    row_pawn = 1 if color == 'black' else 6
    PIECE_POSITIONS = [
      Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
    for i in range(8):
      self.board[i][row_pawn] = Pawn(color)
      self.board[i][row_capital] = PIECE_POSITIONS[i](color)
      
  def move(self, piece, move):
    self.last_move = move
    self.board[move.origin.col][move.origin.row] = None
    self.board[move.target.col][move.target.row] = piece
    piece.moved = True
    for col in self.board:
      for square in col:
        if square: square.enP = False

    if isinstance(piece,Pawn):
      if abs(move.origin.row - move.target.row) == 2:
        piece.enP = True
      
      if self.board[move.target.col][move.origin.row]:
        if self.board[move.target.col][move.origin.row].enP:
          self.board[move.target.col][move.origin.row] = None
      
    for col in self.board:
      for square in col:
        if square: square.enP = False
    
