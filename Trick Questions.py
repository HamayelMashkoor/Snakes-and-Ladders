import random
import time

right_answers = {
    'correct': ['Spot-on!', 'Bingo!', 'Nailed it!', "You're a genius!", 'Right on the money!', 'Brilliant!',
                'You hit the bullseye!', 'Smashing!', 'Way to go!', 'Absolutely', 'right-o!', 'Perfecto!',
                'Spotless victory!', "You're the champ!", 'Precisely!', 'Eureka!'],
    'incorrect': ['Oops-a-daisy!', 'Not quite there, buddy!', 'Uh-oh! Try again!', 'Not the winning ticket!',
                   'Missed it by a hair!', 'Not the magic word!', 'A bit off the mark!', 'Nice try, but not quite!',
                   'Almost, but not quite right!', 'Not hitting the bullseye today!', 'Close, but no cigar!',
                   'Nope, not this time!', 'Missed the boat on that one!', 'Better luck next time!',
                   'Not the golden answer!']
}

questions = [
    {'question': 'What color can you eat?', 'answer': 'Orange'},
    {'question': 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?',
     'answer': 'Echo'},
    {'question': 'The more you take, the more you leave behind. What am I?', 'answer': 'Footsteps'},
    {'question': "I'm tall when I'm young, and short when I'm old. What am I?", 'answer': 'Candle'},
    {'question': 'I can be cracked, made, told, and played. What am I?', 'answer': 'Joke'},
    {'question': 'I fly without wings, I cry without eyes. Wherever I go, darkness follows me. What am I?', 'answer': 'Cloud'},
    {'question': "I have keys but no locks. I have space but no room. You can enter, but you can't go inside. What am I?",
     'answer': 'Keyboard'},
    {'question': "What has a heart that doesn't beat?", 'answer': 'Artichoke'},
    {'question': 'I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?',
     'answer': 'Map'},
    {'question': "What has keys but can't open locks?", 'answer': 'Piano'},
    {'question': 'I have a head, a tail, but no body. What am I?', 'answer': 'Coin'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'Glove'},
    {'question': "What comes once in a minute, twice in a moment, but never in a thousand years?", 'answer': "m"},
    {'question': "How many times can you take 2 apples from a pile of 10 apples?", 'answer': '1'}
]

print("You have a total of 14 tricky questions. Answer at least 7 correctly to win the game.")
time.sleep(1)


def play_game(questions, score=0, rounds=0):
    if rounds == 14:
        print("\nGame Over!")
        print("Your score is:", score)
        print("But you can move forward!")
        return
    if score > 6:
        print("You Won!")
        return

    random.shuffle(questions)
    current_question = questions[0]

    print("\nQuestion:", current_question['question'])
    input_answer = input("Your answer: ")

    if input_answer.lower() == current_question['answer'].lower():
        print(random.choice(right_answers['correct']))
        score += 1
        print("Score:", score)
    else:
        print(random.choice(right_answers['incorrect']))
        print("Score:", score)

    play_game(questions[1:], score, rounds + 1)


play_game(questions)


