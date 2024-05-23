import random
import time


def display_move():
    c = random.randint(1, 3)
    if c == 1:
        return 'ROCK'
    elif c == 2:
        return 'PAPER'
    else:
        return 'SCISSORS'


def player_move():
    p = str(input('Enter Your Move: ...(R)ock, (P)aper, (S)cissors').strip())
    p = p.upper()
    if p == 'R':
        return 'ROCK'
    elif p == 'P':
        return 'PAPER'
    elif p == 'S':
        return 'SCISSORS'
    else:
        return 'Invalid Move'


def play_game():
    print("Its your chance to play Rock Paper Scissor with the computer.")
    time.sleep(1)
    wins = 0
    losses = 0
    ties = 0
    ranges = 3
    won = 0
    while won != 1:
        while ranges > 0:
            player = player_move()
            computer = display_move()
            if player == computer:
                ties += 1
                print("It's a TIE!")
                ranges -= 1
            elif player == 'PAPER' and computer == 'ROCK':
                print('PAPER VERSUS...')
                time.sleep(0.25)
                print('ROCK')
                time.sleep(0.25)
                print('You WIN!')
                ranges -= 1
                wins += 1
            elif player == 'ROCK' and computer == 'SCISSORS':
                print('ROCK VERSUS...')
                time.sleep(0.25)
                print('SCISSORS')
                time.sleep(0.25)
                print('You WIN!')
                ranges -= 1
                wins += 1
            elif player == 'SCISSORS' and computer == 'PAPER':
                print('SCISSORS VERSUS...')
                time.sleep(0.25)
                print('PAPER')
                time.sleep(0.25)
                print('You WIN!')
                wins += 1
                ranges -= 1
            elif player == 'ROCK' and computer == 'PAPER':
                print('ROCK VERSUS...')
                time.sleep(0.25)
                print('PAPER')
                time.sleep(0.25)
                print('You LOSE!')
                losses += 1
                ranges -= 1
            elif player == 'SCISSORS' and computer == 'ROCK':
                print('SCISSORS VERSUS...')
                time.sleep(0.25)
                print('ROCK')
                time.sleep(0.25)
                print('You LOSE!')
                losses += 1
                ranges -= 1
            elif player == 'PAPER' and computer == 'SCISSORS':
                print('PAPER VERSUS...')
                time.sleep(0.25)
                print('SCISSORS')
                time.sleep(0.25)
                print('You LOSE!')
                losses += 1
                ranges -= 1
            else:
                print('Invalid Move')
                print('Please try again...')

        print('{} Wins, {} losses, {} ties'.format(wins, losses, ties))
        if wins > losses:
            won = 1
            print("CONGRATULATIONS! YOU'RE THE WINNER!")
            break
        elif losses > wins:
            ranges = 3
            wins = 0
            losses = 0
            ties = 0
            print("OOPS, YOU LOST! BETTER LUCK NEXT TIME!")
            print()
            print("You will have to play the game again.")
            print()
            time.sleep(2)
        else:
            wins = 0
            losses = 0
            ranges = 3
            ties = 0
            print("IT'S A TIE!")
            print()
            print("You will have to play the game again.")
            print()
            time.sleep(2)


play_game()
