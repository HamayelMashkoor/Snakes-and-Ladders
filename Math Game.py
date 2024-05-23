import random
import time


def mental_math():
    won = 0
    while won != 1:
        print("You have a total time of", 1, "minute. Answer at least", 10, "questions to win the game. Best of Luck")
        time.sleep(2)

        time_limit = 60
        start_time = time.time()

        count = 1
        correct = 0
        while time.time() - start_time <= time_limit:
            list_operations = ["+", "-"]
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            if num1 < 11 or num2 < 11:
                list_operations.append("*")
            elif num1 % num2 == 0:
                list_operations.append("/")
            operation = random.choice(list_operations)
            expression = str(num1) + ' ' + operation + ' ' + str(num2)
            print("Q"+str(count)+") "+expression)
            correct_answer = eval(expression)
            answer = input("Answer?").strip()
            count += 1
            if answer.isdigit() or answer[1:].isdigit():
                if int(answer) == correct_answer:
                    print("Correct!")
                    correct += 1
                else:
                    print("Incorrect. The correct answer is", correct_answer)
            else:
                print("Incorrect. The correct answer is", correct_answer)

        print()
        print("You have exceeded the time limit. Wait while we load your results.")
        print()
        time.sleep(3)
        if correct >= 10:
            print("You scored a total of", correct, " correct questions. Congrats. You win.")
            won = 1
            break
        else:
            print("Sorry, you lose. You could only answer", correct, "questions correctly.")
            print()
            print("You will have to play the game again.")
            time.sleep(2)
            print()


mental_math()
