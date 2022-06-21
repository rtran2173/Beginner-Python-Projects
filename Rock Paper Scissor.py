import random

def play():
    user = input("Select your choice: 'r' for rock, 'p' for paper, 's' for scissor\n")
    ai = random.choice(['r','p','s'])

    if user == ai:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if win(user, ai):
        return "You win"

    return "You lost"

def win(player, opponent):
# return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())