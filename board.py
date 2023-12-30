class Board:
    WIDTH = 8
    HEIGHT = 10

    def __init__(self, chesspieces, white_king_moved, black_king_moved):
        self.chesspieces = chesspieces
        self.white_king_moved = white_king_moved
        self.black_king_moved = black_king_moved
    
    @classmethod
    def clone(cls):
        chess_peices = [[o for x in range(Board.WIDTH) for y in range(Board.HEIGHT)]]