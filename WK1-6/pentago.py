import numpy as np

def initialize_board():
    return np.zeros((6, 6), dtype=int)

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def check_win(board, player):
    for i in range(6):
        for j in range(6):
            if (
                (i + 4 < 6 and np.all(board[i:i+5, j] == player)) or
                (j + 4 < 6 and np.all(board[i, j:j+5] == player)) or
                (i + 4 < 6 and j + 4 < 6 and np.all(np.diag(board[i:i+5, j:j+5]) == player)) or
                (i + 4 < 6 and j - 4 >= 0 and np.all(np.diag(np.fliplr(board[i:i+5, j-4:j+1])) == player))
            ):
                return True
    return False

def place_marble(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0-5) to place your marble: "))
            col = int(input(f"Player {player}, enter the column (0-5) to place your marble: "))
            if board[row, col] == 0:
                board[row, col] = player
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def rotate_quadrant(board, player):
    while True:
        try:
            quad_row = int(input(f"Player {player}, enter the quadrant row (0-1) to rotate: "))
            quad_col = int(input(f"Player {player}, enter the quadrant column (0-1) to rotate: "))
            if 0 <= quad_row < 2 and 0 <= quad_col < 2:
                board[3*quad_row:3*quad_row+3, 3*quad_col:3*quad_col+3] = np.rot90(board[3*quad_row:3*quad_row+3, 3*quad_col:3*quad_col+3], k=1)
                break
            else:
                print("Invalid quadrant. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def apply_move(board, turn, row, col, rot):
    if board[row, col] == 0:
        board[row, col] = turn
        board[3*row:3*row+3, 3*col:3*col+3] = np.rot90(board[3*row:3*row+3, 3*col:3*col+3], k=rot)
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

def menu():
    board = initialize_board()
    player = 1

    print("Welcome to Pentago!")

    while True:
        print_board(board)
        if player == 1:
            print(f"Player {player}'s turn:")
            place_marble(board, player)
        else:
            print("Computer's turn:")
            # Adjust the computer's move logic based on the desired level.
            row, col, rot = computer_move(board, player, level=1)
            print(f"Computer plays: row {row}, col {col}, rotation {rot}")
            apply_move(board, player, row, col, rot)

        if check_win(board, player):
            print_board(board)
            if player == 1:
                print(f"Player {player} wins!")
            else:
                print("Computer wins!")
            break

        rotate_quadrant(board, player)
        player = 3 - player  # Switch player (1 -> 2, 2 -> 1)

    print_board(board)
    print("It's a tie!")



def main():
    board = initialize_board()
    player = 1

    print("Welcome to Pentago!")

    for _ in range(36):
        print_board(board)
        place_marble(board, player)
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        rotate_quadrant(board, player)
        player = 3 - player  # Switch player (1 -> 2, 2 -> 1)

    else:
        print_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    main()