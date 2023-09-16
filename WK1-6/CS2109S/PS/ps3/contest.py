from typing import List, Tuple
import utils

# Define the Score and Move types
Score = int
Move = Tuple[Tuple[int, int], Tuple[int, int]]

class PlayerAI:

    def make_move(self, board) -> Move:
        def evaluate(board):
            bcount = 0
            wcount = 0
            
            for r, row in enumerate(board):
                for c, tile in enumerate(row):
                    if tile == 'B':
                        bcount += 1
                        
                        if r + 1 < 6 and (board[r + 1][c] == 'W' or (c - 1 >= 0 and board[r + 1][c - 1] == 'W') or (c + 1 < 6 and board[r + 1][c + 1] == 'W')):
                            wcount -= 1
                    elif tile == 'W':
                        wcount += 1
                        
                        if r - 1 >= 0 and (board[r - 1][c] == 'B' or (c - 1 >= 0 and board[r - 1][c - 1] == 'B') or (c + 1 < 6 and board[r - 1][c + 1] == 'B')):
                            bcount -= 1
            
            if wcount == 0:
                return utils.WIN
            
            if bcount == 0:
                return -utils.WIN
            
            if any(tile == 'B' for row in board for tile in row):
                return bcount - wcount
            
            if any(tile == 'W' for row in board for tile in row):
                return -utils.WIN
            
            return bcount - wcount

        def minimax(board, depth, max_depth, is_black: bool) -> tuple:
            if depth == max_depth or utils.is_game_over(board):
                evaluation = evaluate(board)
                return evaluation, None

            best_move = None
            if is_black:
                best_score = float('-inf')
            else:
                best_score = float('inf')

            valid_moves = generate_valid_moves(board)

            for move in valid_moves:
                src, dst = move
                src_row, src_col = src
                dst_row, dst_col = dst

                new_board = [row[:] for row in board]
                new_board[dst_row][dst_col] = new_board[src_row][src_col]
                new_board[src_row][src_col] = '_'

                score, _ = minimax(new_board, depth + 1, max_depth, not is_black)
                
                if is_black:
                    if score > best_score:
                        best_score = score
                        best_move = move
                    if score == utils.WIN:
                        return best_score, best_move
                else:
                    if score < best_score:
                        best_score = score
                        best_move = move
                    if score == -utils.WIN:
                        return best_score, best_move

            return best_score, best_move

        def generate_valid_moves(board):
            valid_moves = []
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == 'B':
                        if row + 1 < len(board) and board[row + 1][col] == '_':
                            valid_moves.append(((row, col), (row + 1, col)))
                        if row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] in ('_', 'W'):
                            valid_moves.append(((row, col), (row + 1, col - 1)))
                        if row + 1 < len(board) and col + 1 < len(board[row]) and board[row + 1][col + 1] in ('_', 'W'):
                            valid_moves.append(((row, col), (row + 1, col + 1)))
            return valid_moves

        best_score, best_move = minimax(board, depth=0, max_depth=3, is_black=True)
        return best_move

# Create an instance of your PlayerAI class
ai_player = PlayerAI()
