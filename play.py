from hole import *
import sys

class Play():    
    def generate_board(self, num_hole, init_stone):
        board = []
        for position in range(1, num_hole+1):
            board.append(PlayerHole(init_stone, position))
        board.insert(int(num_hole/2), SideHole("right"))
        board.append(SideHole("left"))

        return board
    
    def __init__(self, num_hole, init_stone):
        self.num_hole = num_hole
        self.init_stone = init_stone
        self.board = self.generate_board(num_hole, init_stone)
        self.your_side = self.board[0:int(self.num_hole/2)]
        self.opponent_side = self.board[int(self.num_hole/2+1):-1]
        self.right_hole = self.board[int(self.num_hole/2)]
        self.left_hole = self.board[-1]

    def sowing(self):
        print("please input the position number where you want to move stones there")
        position = int(input("position number>> "))
        if(position <= int(self.num_hole/2)):
            self.board[position-1].sow(self.board, position, self.num_hole)
        else:
            self.board[position].sow(self.board, position, self.num_hole)

    def view_board(self):
        for hole in reversed(self.opponent_side):
            print("  ", hole.num_stone, end="")
        print("")
        print(self.left_hole.num_stone, "           ", self.right_hole.num_stone)
        for hole in self.your_side:
            print("  ", hole.num_stone, end="")
        print("")

if __name__ == "__main__":
    num_hole = 6
    init_stone = 2
    play = Play(num_hole, init_stone)
    play.sowing()
    play.view_board()
    play.sowing()
    play.view_board()
    play.sowing()
    play.view_board()
    play.sowing()
    play.view_board()
