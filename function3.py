from function0 import display_board


def get_human_coordinates(board, current_player):
    while True:
        move = []
        coordinates = input(f"Make your move, player {current_player}(A/B/C + 1/2/3)\n").upper()
        if coordinates == 'QUIT':
            exit()
        elif len(coordinates) != 2 or coordinates[0] not in ['A', 'B', 'C'] or coordinates[1] not in ['1', '2', '3']:
            print("\nInvalid input. Try again.")
            display_board(board)
        else:
            move.extend([coordinates[0], coordinates[1]])
            if move[0] == "A":
                move[0] = 0
            elif move[0] == "B":
                move[0] = 1
            elif move[0] == "C":
                move[0] = 2
            move[1] = int(move[1]) - 1
            if board[move[0]][move[1]] in ('X', 'O'):
                print("\nThis field is filled in already. Try again.")
                display_board(board)
            else:
                return move[0], move[1]


if __name__ == "__main__":
    board_1 = [
        ["X", "X", "."],
        ["X", ".", "."],
        ["X", "X", "."],
    ]
    coordinates = get_human_coordinates(board_1, "X")
    print(coordinates)  # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones
