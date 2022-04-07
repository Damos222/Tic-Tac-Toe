from function6 import get_winning_player
import random
import copy


def get_mediocre_ai_coordinates(board, current_player):
    print(f"It's AI {current_player}'s move...")
    random_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    list_choose = []
    for x in random_list:
        if board[x[0]][x[1]] == '.':
            list_choose.append(x)
    for x in list_choose:
        board_save = copy.deepcopy(board)
        board_save[x[0]][x[1]] = current_player
        if get_winning_player(board_save) == current_player:
            return x
    for x in list_choose:
        if current_player == 'X':
            other_player = 'O'
        else:
            other_player = 'X'
        board_save = copy.deepcopy(board)
        board_save[x[0]][x[1]] = other_player
        if get_winning_player(board_save) == other_player:
            return x
    if len(list_choose) == 0:
        return None
    else:
        chosen = random.choice(list_choose)
        return chosen

    """
    Should return a tuple of 2 numbers.
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    The chosen coordinate should always stop the other player from winning or
    maximize the current player's chances to win.
    If the board is full (all spots taken by either X or O) than "None"
    should be returned.
    """
    pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
      [".", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print(get_mediocre_ai_coordinates(board_1, "X"))  # the printed coordinate should always be (0, 0)

    board_2 = [
      ["X", "O", "."],
      ["X", ".", "."],
      ["O", "O", "X"],
    ]
    print(get_mediocre_ai_coordinates(board_2, "O"))  # the printed coordinate should always be (1, 1)

    board_3 = [
      ["O", "O", "."],
      ["O", "X", "."],
      [".", "X", "."],
    ]
    print(get_mediocre_ai_coordinates(board_3, "X"))  # the printed coordinate should be either (0, 2) or (2, 0)
