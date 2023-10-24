import numpy as np
import random

# Define constants for player 1 and player 2
PLAYER_1 = 1
PLAYER_2 = 2

# Define the game board as a 6x6 NumPy array
board = np.zeros((6, 6), dtype=int)

def display_board():
    for row in range(6):
        for col in range(6):
            if board[row, col] == PLAYER_1:
                print("X", end=" ")
            elif board[row, col] == PLAYER_2:
                print("O", end=" ")
            else:
                print(".", end=" ")  # You can use any character for empty spaces
        print()  # Move to the next row
    
def check_victory(board,turn,rot):
    # implement your function here
    return -1

def apply_move(board, turn, row, col, rot):
    # Ensure the move is valid before applying it
    if check_move(board, row, col):
        # Place the marble of the current player (1 or 2) in the specified cell
        board[row, col] = turn
        
        # Apply the rotation to the corresponding sub-board
        apply_rotation(board, row, col, rot)
    
    return board

def apply_rotation(board, row, col, rot):
    # Determine the sub-board coordinates
    sub_row = row // 3
    sub_col = col // 3
    
    # Determine the rotation direction (clockwise or counterclockwise)
    clockwise = rot <= 4
    
    # Determine the number of rotations (1 to 4)
    num_rotations = rot % 4
    
    # Rotate the sub-board
    sub_board = board[sub_row * 3: (sub_row + 1) * 3, sub_col * 3: (sub_col + 1) * 3]
    sub_board = np.rot90(sub_board, num_rotations, axes=(1, 0 if clockwise else 1))
    board[sub_row * 3: (sub_row + 1) * 3, sub_col * 3: (sub_col + 1) * 3] = sub_board

    
def check_move(board, row, col):
    # Check if row and col are within valid bounds (0 to 5)
    if 0 <= row < 6 and 0 <= col < 6:
        # Check if the cell is empty (0 represents an empty cell)
        if board[row, col] == 0:
            return True  # Move is valid
    return False  # Move is not valid


def computer_move(board,turn,level):
    # implement your function here
    return (0,0,0)

def menu():  
    # implement your function here
    pass

if __name__ == "__main__":
    menu()
    