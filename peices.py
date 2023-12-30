import board

class Peice():
    WHITE = "W"
    BLACK = "B"

    def __init__(self, x, y, color, peice_type, value):
        self.x = x
        self.y = y
        self.color = color
        self.peice_type = peice_type
        self.value = value

    def get_possible_diagonal_moves(self, board):
        moves = []
        for i in range(1, 8):
            if(not board.in_bounds(self.x+i, self.y+i)):
                break
            piece = board.get_possible_diagonal_moves(self.x+i, self.y+i)
            moves.append(self.get_possible_diagonal_moves(board, self.x+i, self.y+i))
            if (piece != 0):
                break

        for i in range(1, 8):
            if(not board.in_bounds(self.x+i, self.y+i)):
                break
            piece = board.get_possible_diagonal_moves(self.x+i, self.y+i)
            moves.append(self.get_possible_diagonal_moves(board, self.x+i, self.y+i))
            if (piece != 0):
                break
            
        for i in range(1, 8):
            if(not board.in_bounds(self.x-i, self.y-i)):
                break
            piece = board.get_possible_diagonal_moves(self.x-i, self.y-i)
            moves.append(self.get_possible_diagonal_moves(board, self.x+i, self.y+i))
            if (piece != 0):
                break
        
        for i in range(1, 8):
            if(not board.in_bounds(self.x-i, self.y-i)):
                break
            piece = board.get_possible_diagonal_moves(self.x-i, self.y-i)
            moves.append(self.get_possible_diagonal_moves(board, self.x+i, self.y+i))
            if (piece != 0):
                break

        return self.remove_null_from_list(self, moves)


    def get_move(self, board, xto, yto):
        move = 0
        if(board.in_bounds(xto, yto)):
            piece = board.get_piece(xto, yto)
            if (piece != 0):
                if (piece.color != self.color):
                    pass
                else : 
                    pass
        return move
    
    def remove_null_from_list(self, l):
        return [move for move in l if move != 0]

    def to_string(self):
        return self.color + self.piece_type + " "