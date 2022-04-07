def get_winning_player(board):
    winning_player = None
    for row in board:
        if len(set(row)) == 1 and '.' not in row:
            winning_player = row[0]
    for i in range(3):
        if board[0][i] != '.' and board[0][i] == board[1][i] == board[2][i]:
            winning_player = board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        winning_player = board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        winning_player = board[0][2]
    return winning_player


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print(get_winning_player(board_1))  # should return "X"

    board_2 = [
        ["X", "O", "O"],
        ["X", "O", "."],
        ["O", "X", "X"],
    ]
    print(get_winning_player(board_2))  # should return "O"

    board_3 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print(get_winning_player(board_3))  # should return None
