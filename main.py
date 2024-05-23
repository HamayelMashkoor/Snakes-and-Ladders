import random
import subprocess

GAME_BOARD = [['*', '*', 'G', '*', 'F'], ['L', 'G', '*', '*', 'S'], ['*', '*', 'G', '*', '*'], ['G', 'L', 'S', 'G', '*'], ['*', 'G', '*', '*', '*']]


def display_map(grid, player_position) -> None:

    from copy import deepcopy
    displayed_map = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == "S":
                displayed_map[i][j] = '🐍'

            if grid[i][j] == "L":
                displayed_map[i][j] = '⬆'

            if grid[i][j] == "*":
                displayed_map[i][j] = '🟧'

            if grid[i][j] == "F":
                displayed_map[i][j] = '🏆'

            if grid[i][j] == "G":
                displayed_map[i][j] = '🎮'

            if i == player_position[0] and j == player_position[1]:
                displayed_map[i][j] = '♟'

    for row in displayed_map:
        for element in row:
            print(element, end="")
        print()


def snakes_and_ladders(game_board, player_position):
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if i == player_position[0] and j == player_position[1]:
                if game_board[i][j] == "S":
                    player_position[0] += 1
                    print("Oops, the snake bit you.")
                if game_board[i][j] == "L":
                    player_position[0] -= 1
                    print("Hurray, you got a jump towards the top.")


def change_player_position(game_board, player_position):
    answer = input("Your dice is rolling. Press any key to continue.")
    dice = random.randint(1, 6)
    print("You rolled a " + str(dice))

    while dice > 0:
        if player_position[0] % 2 == 0:
            if player_position[0] == 0:
                if player_position[1]+dice > 4:
                    print("Keep trying!")
                    dice = 0
                else:
                    player_position[1] += 1
                    dice -= 1
            elif (player_position[1]+1) > 4:
                player_position[0] -= 1
                dice -= 1
            elif (player_position[1]+1) <= 4:
                player_position[1] += 1
                dice -= 1

        elif player_position[0] % 2 != 0:
            if (player_position[1]-1) < 0:
                player_position[0] -= 1
                dice -= 1
            elif (player_position[1]-1) >= 0:
                player_position[1] -= 1
                dice -= 1

    snakes_and_ladders(game_board, player_position)


def check_finish(player_position):
    if player_position == [0, 4]:
        return True
    else:
        return False


def games(player_position):
    flag = False
    if player_position == [4, 1]:
        subprocess.run(["python", "RockPaperScissor.py"])
    elif player_position == [0, 2]:
        subprocess.run(["python", "Math Game.py"])
        flag = True
    elif player_position == [1, 1]:
        subprocess.run(["python", "GuessNum.py"])
    elif player_position == [2, 2]:
        subprocess.run(["python", "Hangman.py"])
    elif player_position == [3, 0]:
        subprocess.run(["python", "TicTacToe.py"])
    elif player_position == [3, 3]:
        subprocess.run(["python", "Trick Questions.py"])
    return flag


def main():
    player_position = [4, -1]
    display_map(GAME_BOARD, player_position)
    finish = check_finish(player_position)
    last_game = False

    while not finish:
        change_player_position(GAME_BOARD, player_position)
        display_map(GAME_BOARD, player_position)
        finish = check_finish(player_position)
        if not last_game:
            last_game = games(player_position)

    print("Congratulations, you completed the entire board!You are a champ.")


main()





