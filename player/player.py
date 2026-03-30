import pygame

from actions.actions import get_player_action, get_computer_action, winning_comb
from constants import DAMAGE, MAX_HP

class Player():
    def __init__(self, name, max_hp=MAX_HP, damage=DAMAGE):
        self.name = name
        self.current_hp = max_hp
        self.max_hp = max_hp
        self.damage = damage
        self.action = None

    def get_hit(self, damage):
        self.current_hp -= damage
        hp = self.show_curr_hp()
        print(f"{self.name} takes {damage} damage! Current HP: {hp}")

    def show_curr_hp(self):
        current_hp = int(self.current_hp / self.max_hp * 100)
        return current_hp

    def do_damage(self, opponent):
        if self.action == opponent.action:
            print("It's a tie! No damage dealt.")
        elif winning_comb[self.action] == opponent.action:
            print(f"{self.name} wins the round! {opponent.name} takes {self.damage} damage.")
            opponent.get_hit(self.damage)
        else:
            print(f"{opponent.name} wins the round! {self.name} takes {self.damage} damage.")
            self.get_hit(self.damage)

class ComputerPlayer(Player):
    def __init__(self, name, max_hp=MAX_HP, damage=DAMAGE):
        super().__init__(name, max_hp, damage=DAMAGE)
        self.action = None
    
    def get_hit(self, damage):
        super().get_hit(damage)
        hp = self.show_curr_hp()
        print(f"{self.name} (Computer) takes {damage} damage! Current HP: {hp}")

    def show_curr_hp(self):
        current_hp = int(self.current_hp / self.max_hp * 100)
        return current_hp
    
    def do_damage(self, opponent):
        if self.action == opponent.action:
            print("It's a tie! No damage dealt.")
        elif winning_comb[self.action] == opponent.action:
            print(f"{self.name} (Computer) wins the round! {opponent.name} takes {self.damage} damage.")
            opponent.get_hit(self.damage)
        else:
            print(f"{opponent.name} wins the round! {self.name} (Computer) takes {self.damage} damage.")
            self.get_hit(self.damage)