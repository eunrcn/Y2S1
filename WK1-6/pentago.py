import numpy as np


def initialize_board():
    return np.zeros((6, 6), dtype=int)


def display_board(board):
    for row in board:
        print(" ".join(map(str, row)))


def apply_move(board, turn, row, col, rot):
    # Create a new board to avoid modifying the original
    new_board = board.copy()

    if new_board[row, col] == 0:
        new_board[row, col] = turn
        if np.any(new_board[3 * row:3 * row + 3, 3 * col:3 * col + 3] != 0):
            new_board[3 * row:3 * row + 3, 3 * col:3 * col + 3] = np.rot90(
                new_board[3 * row:3 * row + 3, 3 * col:3 * col + 3], k=rot)

    return new_board


def check_move(board, row, col):
    return board[row, col] == 0


def computer_move(board, turn, level):
    if level == 2:
        # Check for direct wins
        for row in range(6):
            for col in range(6):
                if check_move(board, row, col):
                    new_board = apply_move(board.copy(), turn, row, col, 0)
                    if check_victory(new_board, turn) == turn:
                        return row, col, 0

        # Check for blocking opponent wins
        opponent = 3 - turn
        for row in range(6):
            for col in range(6):
                if check_move(board, row, col):
                    new_board = apply_move(board.copy(), opponent, row, col, 0)
                    if check_victory(new_board, opponent) == opponent:
                        return row, col, 0

    # If no direct wins or blocking moves, play a random valid move
    while True:
        row = np.random.randint(6)
        col = np.random.randint(6)
        if check_move(board, row, col):
            return row, col, np.random.randint(4)  # Random rotation

def display_board(board):
    for row in board:
        print(" ".join(map(str, row)))


def check_victory(board, player, test_case=False):
    if test_case:
        # Check that you are not changing the input
        board_out = board.copy()

    # Check for victory before the rotation
    for i in range(6):
        for j in range(6):
            if (
                # Check rows
                (i + 4 < 6 and np.all(board[i:i+5, j] == player)) or
                # Check columns
                (j + 4 < 6 and np.all(board[i, j:j+5] == player)) or
                # Check diagonal
                (i + 4 < 6 and j + 4 < 6 and np.all(np.diag(board[i:i+5, j:j+5]) == player)) or
                # Check anti-diagonal
                (i + 4 < 6 and j - 4 >=
                 0 and np.all(np.diag(np.fliplr(board[i:i+5, j-4:j+1])) == player))
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
                    (i + 4 < 6 and j - 4 >=
                     0 and np.all(np.diag(np.fliplr(rotated_board[i:i+5, j-4:j+1])) == player))
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


def display_board(board):
    # Create a horizontal border
    border = "+-------" * 6 + "+"

    # Display the top border
    print(border)

    for i, row in enumerate(board):
        # Display row numbers
        print("|", end=" ")

        for j, cell in enumerate(row):
            symbol = " "
            if cell == 1:
                symbol = "X"
            elif cell == 2:
                symbol = "O"

            print(f"{symbol:^6}|", end=" ")

        print("\n" + border)

    print("\n   ", end="")
    for col in range(6):
        print(f"{col:^7}", end="")

    print("\n")


def menu():
    board = initialize_board()
    player = 1

    print("Welcome to Pentago!")

    while True:
        display_board(board)
        if player == 1:
            print(f"Player {player}'s turn:")
            try:
                row = int(input("Enter the row (0-5): "))
                col = int(input("Enter the column (0-5): "))
                rot = int(input("Enter the rotation (0-3): "))
            except ValueError:
                print(
                    "Invalid input. Please enter valid row, column, and rotation values.")
                continue

            if 0 <= row < 6 and 0 <= col < 6 and 0 <= rot < 4:
                board = apply_move(board, player, row, col, rot)
            else:
                print(
                    "Invalid input. Please enter valid row, column, and rotation values.")
        else:
            print("Computer's turn:")
            row, col, rot = computer_move(board, player, level=2)
            print(f"Computer plays: row {row}, col {col}, rotation {rot}")
            board = apply_move(board, player, row, col, rot)

        result = check_victory(board, player)
        if result == 1:
            display_board(board)
            print(f"Player {player} wins!")
            break
        elif result == 2:
            display_board(board)
            print("Computer wins!")
            break
        elif result == 3:
            display_board(board)
            print("It's a draw!")
            break

        player = 3 - player


if __name__ == "__main__":
    menu()
