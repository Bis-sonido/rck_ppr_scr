from time import time, perf_counter
import time
from actions.actions import get_player_action, get_computer_action, winning_comb
from player.player import Player, ComputerPlayer, do_damage
from intro.info import info, continue_to_game

def test_game_2():
    info()
    continue_to_game()
    running = True
    while running:
        player = Player("Player")
        computer = ComputerPlayer("Computer")
        while player.current_hp > 0 and computer.current_hp > 0:
            player.action = get_player_action()
            computer.action = get_computer_action()
            
            do_damage(player, computer)
            time.sleep(1.5)
            

            if player.current_hp <= 0:
                print(f"{computer.name} wins the game!")
            elif computer.current_hp <= 0:
                print(f"{player.name} wins the game!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            running = False


if __name__ == "__main__":
    test_game_2()