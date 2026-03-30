from actions.actions import get_player_action, get_computer_action, winning_comb
from player.player import Player, ComputerPlayer

def test_game():
    running = True
    while running:
        player = Player("Player")
        computer = ComputerPlayer("Computer")
        while player.current_hp > 0 and computer.current_hp > 0:
            player.action = get_player_action()
            computer.action = get_computer_action()
            print(f"{player.name} chooses {player.action.name}")
            print(f"{computer.name} chooses {computer.action.name}")


            if player.action == computer.action:
                print("It's a tie! No damage dealt.")
                print(f"{player.name} HP: {player.show_curr_hp()}")
                print(f"{computer.name} HP: {computer.show_curr_hp()}")
                
            elif winning_comb[player.action] == computer.action:
                print(f"{player.name} wins the round! {computer.name} takes {player.damage} damage.")
                computer.get_hit(player.damage)
            else:
                print(f"{computer.name} wins the round! {player.name} takes {computer.damage} damage.")
                player.get_hit(computer.damage)
        if player.current_hp <= 0:
            print(f"{computer.name} wins the game!")
        else:
            print(f"{player.name} wins the game!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            running = False
            
        

if __name__ == "__main__":
    test_game() 
