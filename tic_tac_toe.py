from function0 import display_board
from function1 import get_menu_option
from function2 import get_empty_board
from function3 import get_human_coordinates
from function4 import get_random_ai_coordinates
from function5 import get_unbeatable_ai_coordinates
from function6 import get_winning_player
from function7 import is_board_full
import random
import time
from mediocre_ai import get_mediocre_ai_coordinates

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_MEDIOCRE_AI = 4
HUMAN_VS_UNBEATABLE_AI = 5
MEDIOCRE_AI_VS_MEDIOCRE_AI = 6


def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    current_player = random.choice(['X', 'O'])
    while is_game_running:
        display_board(board)
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        if game_mode == 1:
            x, y = get_human_coordinates(board, current_player)
            time.sleep(1)
        elif game_mode == 2:
            x, y = get_random_ai_coordinates(board, current_player)
            time.sleep(1)
        elif game_mode == 3:
            if current_player == 'X':
                x, y = get_human_coordinates(board, current_player)
                time.sleep(1)
            else:
                x, y = get_random_ai_coordinates(board, current_player)
                time.sleep(1)
        elif game_mode == 4:
            if current_player == 'X':
                x, y = get_human_coordinates(board, current_player)
                time.sleep(1)
            else:
                x, y = get_mediocre_ai_coordinates(board, current_player)
                time.sleep(1)
        elif game_mode == 5:
            if current_player == 'X':
                x, y = get_human_coordinates(board, current_player)
                time.sleep(1)
            else:
                x, y = get_unbeatable_ai_coordinates(board, current_player)
                time.sleep(1)
        elif game_mode == 6:
            x, y = get_mediocre_ai_coordinates(board, current_player)
            time.sleep(1)

        board[x][y] = current_player

        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)
        if winning_player in ('X', 'O'):
            display_board(board)
            if game_mode == 1:
                print(f'Congrats, player {winning_player}, you won!')
                break
            elif game_mode == 2:
                print(f'Congrats, AI {winning_player}, you won!')
                break
            elif game_mode in (3, 4, 5, 6):
                if winning_player == 'X':
                    print(f'Congrats, player {winning_player}, you won!')
                else:
                    print(f'Congrats, AI {winning_player}, you won!')
                break
        elif its_a_tie:
            display_board(board)
            print("It's a tie!")
            break
    while True:
        new_game = input('New game?(y/n)?\n')
        if new_game == 'y':
            main()
        if new_game == 'n':
            exit()


if __name__ == "__main__":
    main()
