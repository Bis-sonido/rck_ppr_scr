import random
from enum import Enum

class Action(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

winning_comb = {
    Action.Rock: Action.Scissors,
    Action.Paper: Action.Rock,
    Action.Scissors: Action.Paper
}

def get_player_action():
    try:
        choices = [f"- {action.name}" for action in Action]
        print("Choose your action:\n")
        for choice in choices:
            print(choice)
        user_input = input("\nEnter your action: ").lower()
        if user_input == "rock":
            return Action.Rock
        elif user_input == "paper":
            return Action.Paper
        elif user_input == "scissors":
            return Action.Scissors
        else:
            raise ValueError("Invalid action. Please enter rock, paper, or scissors.")
    except ValueError as e:
        print(e)
        return get_player_action()
    
def get_computer_action():
    choice = random.choice(list(Action))
    return choice
    