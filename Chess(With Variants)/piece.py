from const import *

class Piece():
  def __init__(self,color,value):
    self.color = color
    valueSign = 1 if color == 'white' else -1
    self.value = value * valueSign
    self.moves = []
    self.moved = False
    self.setImage()
    self.enP = False

  def setImage(self):
    from const import graphics
    names = {Pawn: 'pawn', Rook: 'rook', Knight: 'knight', Bishop: 'bishop',Queen: 'queen', King: 'king'}
    for classtype, name in names.items():
      if isinstance(self, classtype): 
        break
    self.image = graphics[f'{self.color}_{name}']

  def draw(self, square, surface):
    center = (square.col * SIZE + SIZE// 2,square.row * SIZE + SIZE // 2)
    rect = self.image.get_rect(center = center)
    surface.blit(self.image, rect)

  def onBoard(self,square):
    if square.col < 8 and square.row < 8:
      if square.col > -1 and square.row > -1:
        return True
    return False

  def is_friendly(self,square, board):
    if not board[square.col][square.row]: return False
    return self.color == board[square.col][square.row].color

  def straight_line_moves(self,origin,board,direction):
    target = origin
    while True:
      target = Square(target.col + direction[0],
                     target.row + direction[1])
      move = Move(origin,target)
      if not self.onBoard(target): break
      if board[target.col][target.row]:
        if not self.is_friendly(target,board):
          self.moves.append(move)
        break
      self.moves.append(move)
    
class Pawn(Piece):
  def __init__(self,color):
    self.dir = -1 if color == 'white' else 1
    super().__init__(color, 1.0)

  def update_moves(self,origin,board):
    self.moves = []
    steps = 1 if self.moved else 2
    
    #vertical
    start = origin.row + self.dir
    end = start + (self.dir * steps)
    for row in range(start, end, self.dir):
      if not (0 <= row <= 7) or board[origin.col][row]: break
      target = Square(origin.col, row)
      self.moves.append(Move(origin, target))

    #diagnol
    cols = [origin.col -1, origin.col + 1]
    row = origin.row + self.dir
    for col in cols:
      if not self.onBoard(Square(col, row)): continue
      if not board[col][row]:
        if board[col][origin.row]:
          if not board[col][origin.row].enP: continue
        else: continue
      elif board[col][row].color == self.color: continue
      self.moves.append(Move(origin, Square(col,row)))
    

class Rook(Piece):
  def __init__(self,color):
    super().__init__(color, 5.0)

  def update_moves(self,origin,board):
    self.moves = []
    directions = (UP,DOWN,LEFT,RIGHT)
    for direction in directions:
      self.straight_line_moves(origin, board, direction)

class Knight(Piece):
  def __init__(self,color):
    super().__init__(color, 3.0)

  def update_moves(self,origin,board):
    self.moves = []
    for d_col in [-2,-1, 1, 2]:
      for d_row in [-2, -1, 1, 2]:
        if abs(d_col) == abs(d_row): continue
        square = Square(origin.col + d_col, origin.row + d_row)
        if not self.onBoard(square): continue
        if self.is_friendly(square,board): continue
        self.moves.append(Move(origin,square))
          

class Bishop(Piece):
  def __init__(self,color):
    super().__init__(color, 3.001)
    
  def update_moves(self,origin,board):
    self.moves = []
    directions = (UP_LEFT,DOWN_RIGHT,DOWN_LEFT,UP_RIGHT)
    for direction in directions:
      self.straight_line_moves(origin, board, direction)

class Queen(Piece):
  def __init__(self,color):
    super().__init__(color, 9.0)

  def update_moves(self,origin,board):
    self.moves = []
    directions = (UP,DOWN,LEFT,RIGHT,UP_LEFT,DOWN_RIGHT,DOWN_LEFT,UP_RIGHT)
    for direction in directions:
      self.straight_line_moves(origin, board, direction)

class King(Piece):
  def __init__(self,color):
    super().__init__(color, 110)

  def update_moves(self,origin,board):
    self.moves = []
    for d_col in range(-1, 2):
      for d_row in range(-1, 2):
        if (d_col,d_row) == (0,0): continue
        square = Square(origin.col + d_col,origin.row + d_row)
        if not self.onBoard(square): continue
        #if self.is_friendly(square,board): continue
        self.moves.append(Move(origin, square))

    #castle
    if self.moved: return
    # castle left
    if board[0][origin.row]:
      if not board[0][origin.row].moved:
        if not any([board[i][origin.row] for i in range(1,4)]):
          self.moves.append(Move(origin, Square(2,origin.row)))

    # castle right
    if board[7][origin.row]:
      if not board[7][origin.row].moved:
        if not any([board[i][origin.row] for i in range(5,7)]):
          self.moves.append(Move(origin, Square(6,origin.row)))
      
    