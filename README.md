<!--- testing that this comment isn't showing --->
# Rock, Paper, Scissors Showdown
This is a simple rock, paper, and scissors game, with a little twist. Players have a health bar. Each time you win a round, you damage the opponent. To spice up the game, winning multiple rounds in a row, provides a multiplier increase the damge you deal.

![Terminal showing the game in action.](/images/Gameplay.jpg)

# How Does It Work
The player and the computer are their own class with multiple parameters. The important parameters like **damage** and **hp** are defined in my **constants** file.

```python
DAMAGE = 10
MAX_HP = 100

#multipliers are here as well
TWO_W_IN_ROW = 1.5
THREE_W_IN_ROW = 2
```
This allows me to easily adjust the numbers if the game takes too long or vice versa.

### The Loop

The `do_damage()` function handles the majority of the action. This is where the mutliplier logic takes place.

```python

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
# the "else" statement follows after
```

# How To Start

### Clone the Repo
    git clone https://github.com/Bis-sonido/rck_ppr_scr.git
### Run the Code
    ./play.sh
### Have Fun!