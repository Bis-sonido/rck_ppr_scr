import time

from actions.actions import get_player_action, get_computer_action, winning_comb
from constants import DAMAGE, MAX_HP, TWO_W_IN_ROW, THREE_W_IN_ROW

class Player():
    def __init__(self, name, max_hp=MAX_HP, damage=DAMAGE, wins_in_row=0):
        self.name = name
        self.current_hp = max_hp
        self.max_hp = max_hp
        self.damage = damage
        self.action = None
        self.wins_in_row = wins_in_row

    def get_hit(self, damage):
        self.current_hp -= damage

    def show_curr_hp(self):
        current_hp = int(self.current_hp / self.max_hp * 100)
        return current_hp

class ComputerPlayer(Player):
    def __init__(self, name, max_hp=MAX_HP, damage=DAMAGE, wins_in_row=0):
        super().__init__(name, max_hp=MAX_HP, damage=DAMAGE, wins_in_row=0)
        self.current_hp = max_hp
        self.action = None
    
    def get_hit(self, damage):
        self.current_hp -= damage

    def show_curr_hp(self):
        current_hp = int(self.current_hp / self.max_hp * 100)
        return current_hp

def two_w_in_row_multi():
    return TWO_W_IN_ROW

def three_w_in_row_multi():
    return THREE_W_IN_ROW

def do_damage(player, opponent):
    if player.action == opponent.action:
        print("It's a tie! No damage dealt.")
        time.sleep(1.5)
        print(f"{player.name} HP: {player.show_curr_hp()} | {opponent.name} HP: {opponent.show_curr_hp()}")
        time.sleep(1.5)
        player.wins_in_row = 0
        opponent.wins_in_row = 0

    elif winning_comb[player.action] == opponent.action:
        player.wins_in_row += 1
        opponent.wins_in_row = 0

        multiplier = 1
        if player.wins_in_row == 2:
            multiplier = two_w_in_row_multi()
            print(f"{player.name} has won 2 rounds in a row! Damage is multiplied by {multiplier}!")
            time.sleep(1.5)
        elif player.wins_in_row == 3:
            multiplier = three_w_in_row_multi()
            print(f"{player.name} has won 3 rounds in a row! Damage is multiplied by {multiplier}!")
            time.sleep(1.5)
        elif player.wins_in_row > 3:
            multiplier = three_w_in_row_multi()
            print(f"{player.name} on a streak of {player.wins_in_row} wins! Keeping up multiplier at {multiplier}!")
            time.sleep(1.5)

        final_damage = int(player.damage * multiplier)

        print(f"{player.name} wins the round! {opponent.name} takes {final_damage} damage.")
        time.sleep(1.5)
        opponent.get_hit(final_damage)
        print(f"{player.name} HP: {player.show_curr_hp()} | {opponent.name} HP: {opponent.show_curr_hp()}")
    else:
        opponent.wins_in_row += 1
        player.wins_in_row = 0

        multiplier = 1
        if opponent.wins_in_row == 2:
            multiplier = two_w_in_row_multi()
            print(f"{opponent.name} has won 2 rounds in a row! Damage is multiplied by {multiplier}!")
            time.sleep(1.5)
        elif opponent.wins_in_row == 3:
            multiplier = three_w_in_row_multi()
            print(f"{opponent.name} has won 3 rounds in a row! Damage is multiplied by {multiplier}!")
            time.sleep(1.5)

        elif opponent.wins_in_row > 3:
            multiplier = three_w_in_row_multi()
            print(f"{opponent.name} on a streak of {opponent.wins_in_row} wins! Keeping up multiplier at {multiplier}!")
            time.sleep(1.5)

        final_damage = int(player.damage * multiplier)

        print(f"{opponent.name} wins the round! {player.name} takes {final_damage} damage.")
        time.sleep(1.5)
        player.get_hit(final_damage)
        print(f"{player.name} HP: {player.show_curr_hp()} | {opponent.name} HP: {opponent.show_curr_hp()}")