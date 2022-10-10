import random


def play():
    while True:
        player_weapon = input("Pick a weapon! 'r' for Rock, 'p' for Paper, 's' for Scissors, 'end' to end game")

        if player_weapon == 'end':
            break

        computer_weapon = random.choice(['r', 'p', 's'])
        determine_winner(player_weapon, computer_weapon)


def determine_winner(player_weapon, computer_weapon):
    if player_weapon == computer_weapon:
        print("It is a tie!")
        return

    if player_weapon == 'r' and computer_weapon == 's' \
            or player_weapon == 'p' and computer_weapon == 'r' \
            or player_weapon == 's' and computer_weapon == 'p':
        print("You win!")
    else:
        print("Computer has selected: " + computer_weapon)
        print("Computer wins!")


if __name__ == '__main__':
    play()