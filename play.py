from hole import PlayerHole, SideHole
import sys

class Play():    
    def generate_board(self, num_hole, init_stone):
        self.player_side = [PlayerHole(init_stone, "player",  position) for position in range(1, num_hole+1)]
        self.opponent_side = [PlayerHole(init_stone, "opponent",  position) for position in range(1, num_hole+1)]
        self.right_hole = SideHole("right")
        self.left_hole = SideHole("left")
        self.board = self.player_side + [self.right_hole] + self.opponent_side + [self.left_hole]
    
    def __init__(self, num_hole, init_stone):
        self.num_hole = num_hole
        self.init_stone = init_stone
        self.generate_board(num_hole, init_stone)

    def sowing(self):
        print("please input the position number where you want to move stones there")
        position = int(input("position number>> "))
        if(position <= self.num_hole):
            self.board[position-1].sow(self.board, position, self.num_hole)
        else:
            self.board[position].sow(self.board, position, self.num_hole)

    def view_board(self):
        for hole in reversed(self.opponent_side):
            print("  ", hole.num_stone, end="")
        print("")
        print(self.left_hole.num_stone, "    "*self.num_hole, self.right_hole.num_stone)
        for hole in self.player_side:
            print("  ", hole.num_stone, end="")
        print("")

if __name__ == "__main__":
    num_hole = 3
    init_stone = 2
    play = Play(num_hole, init_stone)
    play.view_board()
    play.sowing()
    play.view_board()
    play.sowing()
    play.view_board()
    play.sowing()
    play.view_board()
    play.sowing()
    play.view_board()
