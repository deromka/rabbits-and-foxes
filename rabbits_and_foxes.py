from abc import ABC, abstractmethod
from enum import Enum
import colorama
from colorama import Fore

class Color(Enum):
    WHITE = 1
    GRAY = 2
    BROWN = 3




class Block:

    def __init__(self, piece = None):
        self.piece = piece

    def __str__(self):
        return '_'

class Board:

    def __init__(self, blocks=None, rows=5, cols=5):
        if blocks is None:
            self.blocks = [[Block() for i in range(cols)] for j in range(rows)]
        else:
            self.blocks = blocks

    def __str__(self):
        st = '-----------\n'
        for row in self.blocks:
            for elem in row:
               st+=str(elem)+' '
            st+='\n'
        st+='-----------'
        return st

class Piece(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def is_valid_move(self, move, board):
        pass


class ShortPiece(Piece):

    def __init__(self):
        super().__init__()



class LongPiece(Piece):

    def __init__(self):
        super().__init__()



class Move:

    def __init__(self, src : Block, dest : Block, piece : Piece):
        self.src = src
        self.dest = dest
        self.piece = piece





class NotMovablePiece(ShortPiece):

    def is_valid_move(self, move : Move, board : Board):
        return False


class Rabbit(ShortPiece):

    def __init__(self, color: Color):
        self.color = color

    def is_valid_move(self, move : Move, board : Board):
        pass

    def __str__(self):
        return f'R{self.color._value_}'

class Fox(LongPiece):

    def is_valid_move(self, move : Move, board : Board):
        pass

    def __str__(self):
        return 'F'

class Mushroom(NotMovablePiece):

    def __init__(self):
        pass

    def __str__(self):
        return 'M'

#    def __repr__(self):
#        return 'M'


class Hole(NotMovablePiece):

    def __init__(self, piece = None):
        self.piece = piece

    def __str__(self):
        if self.piece is None:
            return 'H'
        else:
            return str(self.piece)

''' 
    A barrier for Foxes only
    Can hold other pieces, except fox  
'''
class FoxBarrier(NotMovablePiece):

    def __init__(self, piece = None ):
        self.piece = piece

    def __str__(self):
        if self.piece is None:
            return 'B'
        else:
            return str(self.piece)




class Level:

    def __init__(self, num, min_num_steps, board : Board):
        self.num = num
        self.board = board
        self.min_num_steps = min_num_steps

    def __str__(self):
        return f'Level {self.num}, Min Steps {self.min_num_steps}\n{str(self.board)}'

class GameStrategy(ABC):

    @abstractmethod
    def next_move(self, board : Board):
        pass


class BackTrackingStrategy(GameStrategy):

    def next_move(self, board : Board):
        pass

class ManualStrategy(GameStrategy):

    def next_move(self, board : Board):
        pass


class Game:

    def __init__(self, level : Level):
        self.board = level.board
        self.is_game_over = False

    def move(self, strategy : GameStrategy):
        strategy.next_move(self.board)

    def play(self):

        current_strategy = BackTrackingStrategy()

        while not self.is_game_over:
            self.move(current_strategy)




if __name__ == '__main__':

    board_level1=Board([[Hole(), Mushroom(), FoxBarrier(Mushroom()), Block(), Hole()],
                        [Block(), Block(), Block(), Mushroom(), Block()],
                        [FoxBarrier(), Block(), Hole(), Rabbit(Color.WHITE), FoxBarrier()],
                        [Block(), Block(), Block(), Block(), Block()],
                        [Hole(), Block(), FoxBarrier(), Block(), Hole()]])
    level1 = Level(1, 2, board_level1)

    print(level1)

    rabbit_and_fox_game = Game(level1)