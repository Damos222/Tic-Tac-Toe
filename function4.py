import random


def get_random_ai_coordinates(board, current_player):
    print(f"It's AI {current_player}'s move...")
    all_rows_full = True
    for row in board:
        if '.' in row:
            all_rows_full = False
    if all_rows_full:
        return None
    invalid = True
    while invalid:
        random_ai_coordinates = (random.choice(range(3)), random.choice(range(3)))
        a = random_ai_coordinates[0]
        b = random_ai_coordinates[1]
        if board[a][b] == '.':
            invalid = False
    return a, b


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
        ["O", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print(get_random_ai_coordinates(board_1, "X"))  # the printed coordinate should be only (0,2) or (1,2)
    print(get_random_ai_coordinates(board_1, "X"))  # the printed coordinate should be only (0,2) or (1,2)
    print(get_random_ai_coordinates(board_1, "X"))  # the printed coordinate should be only (0,2) or (1,2)

    board_2 = [
        ["O", "X", "X"],
        ["X", "O", "X"],
        ["X", "O", "X"],
    ]
    print(get_random_ai_coordinates(board_2, "O"))  # the printed coordinate should be None
