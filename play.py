from hole import *

def sowing(board, position):
    board[position-1].sow(board, position)

def view_board(board):
    for hole in board:
        print(hole.num_stone)

hole_01 = PlayerHole(2, 1)
hole_02 = PlayerHole(2, 2)
hole_03 = PlayerHole(2, 3)
hole_04 = PlayerHole(2, 4)
hole_05 = PlayerHole(2, 5)
hole_06 = PlayerHole(2, 6)
hole_07 = PlayerHole(2, 7)
hole_08 = PlayerHole(2, 8)
hole_09 = PlayerHole(2, 9)
hole_10 = PlayerHole(2, 10)
hole_11 = PlayerHole(2, 11)
hole_12 = PlayerHole(2, 12)
hole_right = SideHole("right")
hole_left = SideHole("left")

board = [hole_01, hole_02, hole_03, hole_04, hole_05, hole_06, hole_right, hole_07, hole_08, hole_09, hole_10, hole_11, hole_12, hole_left]
hole_04.num_stone = 5

sowing(board, 4)
view_board(board)
