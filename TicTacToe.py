import random


def display_tic_tac_toe_board(board):
    print('Welcome to Tic-Tac-Toe!')
    print('Please enter the number of the cell you want to move in')
    print("Your mark is ❌")
    user_player, computer_player = '❌', '⭕'

    while True:
        display_board(board)
        user_move = get_user_move()
        update_board(board, user_move, user_player)

        if check_winner(board, user_player):
            update_board(board, user_move, user_player)
            display_board(board)
            print('Congratulations! You won!')
            break

        if full(board):
            update_board(board, user_move, user_player)
            display_board(board)
            board = [[' ' for _ in range(3)] for _ in range(3)]
            print("It's a tie!")
            print("You need to play again!")

        print("Computer's turn:")
        computer_move = get_computer_move(board)
        update_board(board, computer_move, computer_player)

        if check_winner(board, computer_player):
            update_board(board, user_move, user_player)
            display_board(board)
            board = [[' ' for _ in range(3)] for _ in range(3)]
            print('Computer wins!')
            print("You need to play again!")

        if full(board):
            update_board(board, user_move, user_player)
            display_board(board)
            board = [[' ' for _ in range(3)] for _ in range(3)]
            print("It's a tie!")
            print("You need to play again!")


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def full(board):
    for row in board:
        for column in row:
            if column == ' ':
                return False
    return True


def get_user_move():
    while True:
        move = input("Enter your move (1-9): ").strip()
        if move.isdigit():
            move = int(move)
            if 1 <= int(move) <= 9:
                return move
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def get_computer_move(board):
    available_moves = [i * 3 + j + 1 for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)


def update_board(board, move, player):
    index = move - 1
    row, col = divmod(index, 3)

    if board[row][col] == ' ':
        board[row][col] = player
    else:
        print("Oops! The cell is already occupied. You missed your chance! 👎")


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    display_tic_tac_toe_board(board)


play_game()
