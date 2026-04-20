import random
from enum import Enum
import time

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
        print("\nActions:\n")
        for choice in choices:
            print(choice)
        user_input = input("\nChoose your action: ").lower()
        if user_input == "rock":
            print("\nYou chose Rock", end=" |")
            return Action.Rock
        elif user_input == "paper":
            print("\nYou chose Paper", end=" |")
            return Action.Paper
        elif user_input == "scissors":
            print("\nYou chose Scissors", end=" |")
            return Action.Scissors
        else:
            raise ValueError("\nInvalid action. Please enter rock, paper, or scissors.")
    except ValueError as e:
        print(e)
        time.sleep(1.5)
        return get_player_action()
    
def get_computer_action():
    choice = random.choice(list(Action))
    print(" Computer chose " + choice.name)
    return choice
    