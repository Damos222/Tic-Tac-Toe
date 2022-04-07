def get_menu_option():
    print("Welcome to tic tac toe!")
    while True:
        level = input("""
1. Human vs Human
2. Random AI vs Random AI
3. Human vs Random AI
4. Human vs Hard AI
5. Human vs Unbeatable AI
6. Hard AI vs Hard AI

Choose a game mode(1-6): """)
        if level in ["1", "2", "3", "4", "5", "6"]:
            return int(level)
        else:
            print("\nInvalid input. Please try again.")


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option)  # if the user selected 1, it should print 1
    # lodjfhgalkfjsdh
