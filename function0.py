def display_board(board):
    print("       1   2   3")
    print("A", end="      ")
    print(" | ".join(board[0]))
    print("      ---+---+---")
    print("B", end="      ")
    print(" | ".join(board[1]))
    print("      ---+---+---")
    print("C", end="      ")
    print(" | ".join(board[2]))
    print("      ---+---+---")


"""
    Should print the tic tac toe board in a format similar to
        1   2   3
     A   X | O | .
        ---+---+---
     B   X | O | .
        --+---+---
     C   0 | X | .
        --+---+---
"""


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = [
      ['X', "O", "."],
      ['X', "O", "."],
      ['0', "X", "."]
    ]
    display_board(board)
    # should print
    #     1   2   3
    # A   X | O | .
    #    ---+---+---
    # B   X | O | .
    #    --+---+---
    # C   0 | X | .
    #    --+---+---
