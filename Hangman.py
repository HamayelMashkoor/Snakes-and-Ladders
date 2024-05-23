import random
import time

Category1 = 'Indian Movies'
Words1 = ["KALHONAHO", "DILWALE", "OMSHANTIOM", "KUCHKUCHHOTAHAI"]

Category2 = 'English Movies'
Words2 = ["INCEPTION", "OPENHEIMER", "INTERSTELLAR", "TENET"]


def instructions():
    print("Please read the following instructions carefully:")
    print("You will only be allowed 3 wrong guess per word")
    print("Please enter your guesses wisely 🙏")
    print("Don't worry, you'll be given a hint for each category 😮‍💨")
    print("Remember there are no spaces between each word.")
    print("You Got This! 💪")


def play_game():
    won = 0
    while won != 1:
        instructions()
        input("Press any key to start...")

        category = random.choice([Category1, Category2])

        if category == Category1:
            secret_word = random.choice(Words1)

        else:
            secret_word = random.choice(Words2)

        correct_letters = []
        wrong_letters = []
        word_completion = "_" * len(secret_word.replace(" ", ""))
        print("Category: {}".format(category))
        print(word_completion)
        if category == Category1:
            print("Hint: Try thinking of a SRK BLOCKBUSTER!")
        else:
            print("Hint: Try thinking of a Christopher Nolan BLOCKBUSTER!")

        while True:
            user_guess = input("Guess a letter: ").upper().strip()

            if len(user_guess) != 1 or not user_guess.isalpha():
                print('Try a single letter.')
                continue

            if user_guess in correct_letters or user_guess in wrong_letters:
                print("Try another letter.")
                continue

            if user_guess in secret_word:
                correct_letters.append(user_guess)
                word_completion = "".join(
                    letter if letter in correct_letters or letter.isspace() else "_"
                    for letter in secret_word
                )

                print("Correct letters: {}".format(', '.join(correct_letters)))
                print("Wrong letters: {}".format(', '.join(wrong_letters)))
                print("Word: {}".format(word_completion))

                if "_" not in word_completion:
                    print('Yes! You have guessed the word.')
                    won = 1
                    break
            else:
                wrong_letters.append(user_guess)
                print("Correct letters: {}".format(', '.join(correct_letters)))
                print("Wrong letters: {}".format(', '.join(wrong_letters)))
                print("Word: {}".format(word_completion))

                if len(wrong_letters) == 3:
                    print("OOPS! You Lost!")
                    print("Ýou need to play the game again")
                    time.sleep(2)
                    print()
                    break


play_game()
