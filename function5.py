
from function6 import get_winning_player
from function7 import is_board_full


def get_unbeatable_ai_coordinates(board, current_player):
    print(f"It's AI {current_player}'s move...")
    best = float("-inf")
    for a in range(0, 3):
        for b in range(0, 3):
            if board[a][b] == ".":
                board[a][b] = "O"
                score = minimax(board, current_player)
                board[a][b] = "."
                if score > best:
                    move = (a, b)
                    best = score
    return move


def minimax(board, current_player):
    if get_winning_player(board) == "O":
        return 1
    elif get_winning_player(board) == "X":
        return -1
    elif is_board_full(board):
        return 0
    if current_player == "X":
        current_player = "O"
        best = float("-inf")
        for a in range(0, 3):
            for b in range(0, 3):
                if board[a][b] == ".":
                    board[a][b] = "O"
                    score = minimax(board, current_player)
                    board[a][b] = "."
                    best = max(best, score)
        return best
    if current_player == "O":
        current_player = "X"
        best = float("inf")
        for a in range(0, 3):
            for b in range(0, 3):
                if board[a][b] == ".":
                    board[a][b] = "X"
                    score = minimax(board, current_player)
                    board[a][b] = "."
                    best = min(best, score)
        return best


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
        [".", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
      ]
    print(get_unbeatable_ai_coordinates(board_1, "O"))  # the printed coordinate should always be (0, 0)

    board_2 = [
        ["X", "O", "."],
        ["X", ".", "."],
        ["O", "O", "X"],
      ]
    print(get_unbeatable_ai_coordinates(board_2, "O"))  # the printed coordinate should always be (1, 1)

    board_3 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "X"],
      ]
    print(get_unbeatable_ai_coordinates(board_3, "O"))  # the printed coordinate should be either (0, 2) or (2, 0)
