from hole import *

def generate_board(num_hole, init_stone):
    board = []
    for position in range(1, num_hole+1):
        board.append(PlayerHole(init_stone, position))
    board.insert(int(num_hole/2), SideHole("right"))
    board.append(SideHole("left"))

    return board


def sowing(board, position):
    board[position-1].sow(board, position)

def view_board(board):
    for hole in board:
        print(hole.num_stone)

board = generate_board(12, 2)
board[3].num_stone = 28

sowing(board, 4)
view_board(board)
