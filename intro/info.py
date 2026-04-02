from constants import DAMAGE, TWO_W_IN_ROW, THREE_W_IN_ROW

def info():
    info = print(
f"""
This is Rock-Paper_Scissors with a health bar and damage system.
Each player starts with 100 HP. Winning a round deals {DAMAGE} damage to the opponent.
If a player wins 2 rounds in a row, their damage is multiplied by {TWO_W_IN_ROW}.
If a player wins 3 rounds in a row, their damage is multiplied by {THREE_W_IN_ROW}.
The game continues until a player's HP drops to 0 or below.
The player with remaining HP wins the game. After the game ends, players can choose to play again or exit.
    
Good Luck!
    """)
    return info

def continue_to_game():
    while True:
        user_input = input("Press Enter to continue to the game...")
        if user_input == "":
            break
        else:
            print("Invalid input. Please press Enter to continue.")

