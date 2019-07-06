from hole import *

class Play():    
    def generate_board(self, num_hole, init_stone):
        board = []
        for position in range(1, num_hole+1):
            board.append(PlayerHole(init_stone, position))
        board.insert(int(num_hole/2), SideHole("right"))
        board.append(SideHole("left"))

        return board
    
    def __init__(self, num_hole, init_stone):
        self.board = self.generate_board(num_hole, init_stone)
        self.num_hole = num_hole
        self.init_stone = init_stone

    def sowing(self, position):
        print("---------------sowing(", position, ")---------------")
        if(position <= int(self.num_hole/2)):
            self.board[position-1].sow(self.board, position, self.num_hole)
        else:
            self.board[position].sow(self.board, position, self.num_hole)

    def view_board(self):
        for hole in self.board:
            print(hole.num_stone)

if __name__ == "__main__":
    num_hole = 6
    init_stone = 200
    play = Play(num_hole, init_stone)
    play.sowing(3)
    play.view_board()
    play.sowing(5)
    play.view_board()
    play.sowing(1)
    play.view_board()
    play.sowing(6)
    play.view_board()
