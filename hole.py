class Hole:
    def __init__(self):
        self.num_stone = 0
    
    def sowed(self):
        self.num_stone += 1

class PlayerHole(Hole):
    def __init__(self, num_stone, position):
        self.num_stone = num_stone
        self.position = position

    def sow(self, board, position):
        begin = position
        final = begin + self.num_stone
        for hole in board[begin:final]:
            hole.sowed()
        self.num_stone = 0
 
class SideHole(Hole):
    def __init__(self, position):
        self.num_stone = 0
        self.position = position
