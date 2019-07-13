from hole import PlayerHole, SideHole
import sys

class Play():    
    def __init__(self, num_hole, init_stone):
        """initial function in Play class
        
        Arguments:
            num_hole {int} -- the number of holes on one side except side holes
            init_stone {int} -- the number of stones that is put on each hole by default
        """
        self.num_hole = num_hole
        self.init_stone = init_stone
        self.turn = "Player"
        self.player_side = [PlayerHole(init_stone, "Player",  position) for position in range(1, num_hole+1)]
        self.opponent_side = [PlayerHole(init_stone, "Opponent",  position) for position in range(1, num_hole+1)]
        self.right_hole = SideHole("right")
        self.left_hole = SideHole("left")
        self.board = self.player_side + [self.right_hole] + self.opponent_side + [self.left_hole]

    def sowing(self):
        print(f"<{self.turn}'s turn>")
        print("please input the position number where you want to move stones there")
        position = int(input("position number>> "))
        active_board = self.player_side if self.turn=="Player" else self.opponent_side
        selected_hole = active_board[position-1]
        num_sowed_stone = selected_hole.num_stone
        selected_hole.sow(self.board, position, self.num_hole, self.turn)
        self.does_game_finish(active_board)
        self.change_turn(position, num_sowed_stone)
    
    def change_turn(self, position, num_sowed_stone):
        distance_to_sidehole = self.num_hole - position + 1
        if(distance_to_sidehole == num_sowed_stone):
            pass
        else:
            self.turn = "Player" if self.turn=="Opponent" else "Opponent" 
        self.view_board()
        self.sowing()
    
    def does_game_finish(self, active_board):
        if all(hole.num_stone==0 for hole in active_board):
            self.view_board()
            print(f"{self.turn} Wins!")
            sys.exit()
            

    def view_board(self):
        for hole in reversed(self.opponent_side):
            print("  ", hole.num_stone, end="")
        print("")
        print(self.left_hole.num_stone, "    "*self.num_hole, self.right_hole.num_stone)
        for hole in self.player_side:
            print("  ", hole.num_stone, end="")
        print("")
    
    def start_game(self):
        self.view_board()
        self.sowing()


if __name__ == "__main__":
    num_hole = 3
    init_stone = 2
    play = Play(num_hole, init_stone)
    play.start_game()
