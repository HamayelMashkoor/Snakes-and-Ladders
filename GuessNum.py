import random
import time


def guess_number():
    won = 0
    while won != 1:
        allowed_numbers = [21, 35, 48, 72]
        random_number = random.choice(allowed_numbers)
        print()
        if random_number == 21:
            count = 4
            print("You have a total of 5 chances")
            while count >= 0:
                guess = input("Guess a number between 1 and 30.").strip()
                if guess.isdigit():
                    if count == 0 and int(guess) != 21:
                        print("Sorry, you lost.")
                        print("You have " + str(0) + " chances left. Better luck next time :)")
                        print("You will have to play the game again.")
                        time.sleep(2)
                        break
                    elif int(guess) == 21:
                        print("Congratulations, you won. The correct number is 21.")
                        print("You can proceed towards the board.")
                        won = 1
                        break
                    elif int(guess) <= 10:
                        print("Your guess is too low. Try Again")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 28 <= int(guess) <= 30:
                        print("Your guess is too high. Try Again")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 10 < int(guess) < 28 and int(guess) != 21 and int(guess) % 3 != 0:
                        print("You are close. Try thinking of multiples of 3.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 10 < int(guess) < 28 and int(guess) != 21 and int(guess) % 7 != 0:
                        print("You are close. Try thinking of multiples of 7.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif int(guess) > 30:
                        print("Your number is out of range.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    else:
                        print("Keep trying.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1

        elif random_number == 35:
            count = 4
            print("You have a total of 5 chances")

            guess = input("Guess a number between 20 and 50.").strip()
            if guess.isdigit():
                guess = int(guess)

                if count == 0 and guess != 35:
                    print("Sorry, you lost.")
                    print("You have " + str(0) + " chances left. Better luck next time :)")
                    print("You will have to play the game again.")
                    time.sleep(2)
                    break
                elif guess == 35:
                    print("Congratulations, you won. The correct number is 35.")
                    print("You can proceed towards the board.")
                    won = 1
                elif 20 <= guess <= 25:
                    print("Your guess is too low. Try Again")
                    print("You have " + str(count) + " chances left.")
                    count -= 1
                elif 42 <= guess <= 50:
                    print("Your guess is too high. Try Again")
                    print("You have " + str(count) + " chances left.")
                    count -= 1
                elif 20 < guess < 42 and guess != 35 and guess % 5 != 0:
                    print("You are close. Try thinking of multiples of 5.")
                    print("You have " + str(count) + " chances left.")
                    count -= 1
                elif 20 < guess < 42 and guess != 35 and guess % 7 != 0:
                    print("You are close. Try thinking of multiples of 7.")
                    print("You have " + str(count) + " chances left.")
                    count -= 1
                elif guess > 50 or guess < 20:
                    print("Your number is out of range.")
                    print("You have " + str(count) + " chances left.")
                    count -= 1
                else:
                    print("Keep trying.")
                    print("You have " + str(count) + " chances left.")
                    count -= 1

        elif random_number == 48:
            count = 4
            print("You have a total of 5 chances")
            while count >= 0:
                guess = input("Guess a number between 30 and 60.").strip()
                if guess.isdigit():
                    guess = int(guess)
                    if count == 0 and guess != 48:
                        print("Sorry, you lost.")
                        print("You have " + str(0) + " chances left. Better luck next time :)")
                        print("You will have to play the game again.")
                        time.sleep(2)
                        break
                    elif guess == 48:
                        print("Congratulations, you won. The correct number is 48.")
                        print("You can proceed towards the board.")
                        won = 1
                        break
                    elif 38 >= guess >= 30:
                        print("Your guess is too low. Try Again")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 53 <= guess <= 60:
                        print("Your guess is too high. Try Again")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 38 < guess < 53 and guess != 48 and guess % 6 != 0:
                        print("You are close. Try thinking of multiples of 6.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 38 < guess < 53 and guess != 48 and guess % 8 != 0:
                        print("You are close. Try thinking of multiples of 8.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif guess < 30 or guess > 60:
                        print("Your number is out of range.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    else:
                        print("Keep trying.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1

        elif random_number == 72:
            count = 4
            print("You have a total of 5 chances")
            while count >= 0:
                guess = input("Guess a number between 50 and 85.").strip()
                if guess.isdigit():
                    guess = int(guess)
                    if count == 0 and guess != 72:
                        print("Sorry, you lost.")
                        print("You have " + str(0) + " chances left. Better luck next time :)")
                        print("You will have to play the game again.")
                        time.sleep(2)
                        break
                    elif guess == 72:
                        print("Congratulations, you won. The correct number is 72.")
                        print("You can proceed towards the board.")
                        won = 1
                        break
                    elif 60 >= guess >= 50:
                        print("Your guess is too low. Try Again")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 80 <= guess <= 85:
                        print("Your guess is too high. Try Again")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 60 < guess < 85 and guess != 72 and guess % 9 != 0:
                        print("You are close. Try thinking of multiples of 9.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif 60 < guess < 85 and guess != 72 and guess % 8 != 0:
                        print("You are close. Try thinking of multiples of 8.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    elif guess < 85 or guess > 50:
                        print("Your number is out of range.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1
                    else:
                        print("Keep trying.")
                        print("You have " + str(count) + " chances left.")
                        count -= 1


guess_number()
