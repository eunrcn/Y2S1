import numpy as np

def initialize_board():
    return np.zeros((6, 6), dtype=int)

def display_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def apply_move(board, turn, row, col, rot):
    if board[row, col] == 0:
        board[row, col] = turn
        if np.any(board[3 * row:3 * row + 3, 3 * col:3 * col + 3] != 0):
            board[3 * row:3 * row + 3, 3 * col:3 * col + 3] = np.rot90(board[3 * row:3 * row + 3, 3 * col:3 * col + 3], k=rot)
    return board

def check_move(board, row, col):
    return board[row, col] == 0

def computer_move(board, turn, level):
    # Implement computer's move logic here based on the provided level
    # For example, you can generate random valid moves for level 1.
    # For more advanced levels, you can implement a smarter AI.

    # For now, let's assume a simple random move for demonstration.
    while True:
        row = np.random.randint(6)
        col = np.random.randint(6)
        if check_move(board, row, col):
            return row, col, np.random.randint(4)  # Random rotation
        
def display_board(board):
    for row in board:
        print(" ".join(map(str, row)))

import numpy as np

def check_victory(board, player, test_case=False):
    if test_case:
        # Check that you are not changing the input
        board_out = board.copy()
    
    # Check for victory before the rotation
    for i in range(6):
        for j in range(6):
            if (
                (i + 4 < 6 and np.all(board[i:i+5, j] == player)) or  # Check rows
                (j + 4 < 6 and np.all(board[i, j:j+5] == player)) or  # Check columns
                (i + 4 < 6 and j + 4 < 6 and np.all(np.diag(board[i:i+5, j:j+5]) == player)) or  # Check diagonal
                (i + 4 < 6 and j - 4 >= 0 and np.all(np.diag(np.fliplr(board[i:i+5, j-4:j+1])) == player))  # Check anti-diagonal
            ):
                return player  # Player wins

    # Apply rotation and check for victory after the rotation
    for rot in range(1, 9):
        rotated_board = np.rot90(board, k=rot)
        for i in range(6):
            for j in range(6):
                if (
                    (i + 4 < 6 and np.all(rotated_board[i:i+5, j] == player)) or
                    (j + 4 < 6 and np.all(rotated_board[i, j:j+5] == player)) or
                    (i + 4 < 6 and j + 4 < 6 and np.all(np.diag(rotated_board[i:i+5, j:j+5]) == player)) or
                    (i + 4 < 6 and j - 4 >= 0 and np.all(np.diag(np.fliplr(rotated_board[i:i+5, j-4:j+1])) == player))
                ):
                    return player  # Player wins

    if not test_case:
        # Check for a draw (full board with no winner)
        if np.all(board != 0):
            return 3  # Draw

    # No winner yet
    return 0




def is_draw(board):
    # Check if the board is full (no empty spaces)
    return np.all(board != 0)

def menu():
    board = initialize_board()
    player = 1

    print("Welcome to Pentago!")

    while True:
        display_board(board)
        if player == 1:
            print(f"Player {player}'s turn:")
            row = int(input("Enter the row (0-5): "))
            col = int(input("Enter the column (0-5): "))
            rot = int(input("Enter the rotation (0-3): "))
            apply_move(board, player, row, col, rot)
        else:
            print("Computer's turn:")
            row, col, rot = computer_move(board, player, level=1)
            print(f"Computer plays: row {row}, col {col}, rotation {rot}")
            apply_move(board, player, row, col, rot)

        # Check for victory and draw within the loop
        result = check_victory(board, player)
        if result == 1:
            display_board(board)
            if player == 1:
                print(f"Player {player} wins!")
            else:
                print("Computer wins!")
            break
        elif result == 2:
            display_board(board)
            print("Computer wins!")
            break
        elif result == 3:
            display_board(board)
            print("It's a draw!")
            break

        player = 3 - player  # Switch player (1 -> 2, 2 -> 1)

if __name__ == "__main__":
    menu()