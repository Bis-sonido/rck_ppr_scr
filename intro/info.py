from constants import DAMAGE, TWO_W_IN_ROW, THREE_W_IN_ROW

def info():
    info = print(
f"""
This is Rock, Paper, Scissors Showdown.
Each player starts with 100 HP. Winning a round deals {DAMAGE} damage to the opponent.
If a player wins 2 rounds in a row, their damage is multiplied by {TWO_W_IN_ROW}.
If a player wins 3 rounds in a row, their damage is multiplied by {THREE_W_IN_ROW}.
The game continues until a player's HP drops to 0 or below.
The player with remaining HP wins the game.
    """)
    return info

def continue_to_game():
    while True:
        user_input = input("Would you like to continue to the game? (yes/no): ").lower()
        if user_input == "yes":
            print("\nGood luck!")
            break
        elif user_input == "no":
            print("Maybe next time!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
