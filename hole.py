class Hole:
    def __init__(self):
        self.num_stone = 0
    
    def sowed(self):
        self.num_stone += 1

class PlayerHole(Hole):
    def __init__(self, num_stone, side, position):
        self.num_stone = num_stone
        self.side = side
        self.position = position

    def sow(self, board, position, num_hole, turn):
        rotation = -(-self.num_stone // len(board)) + 1
        board = board * rotation
        begin = position if turn=="Player" else position+num_hole+1
        final = begin+self.num_stone
        self.num_stone = 0
        for hole in board[begin: final]:
            hole.sowed() 
 
class SideHole(Hole):
    def __init__(self, position):
        self.num_stone = 0
        self.position = position