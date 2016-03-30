#
# import random
#
# answer = random.randint(1, 2)
#
# print('This is a guessing game')
# print('Guess a number:')
#
# guess = int(input())
#
# while guess != answer:
#     if guess > answer:
#         print('Too high, dude.')
#     elif guess < answer:
#         print('Too low, yo.')
#     print('Guess again:')
#     guess = int(input())
# if guess == answer:
#     print('Correct! You are a winner!')

########

import random
def generate_answer():
    """Generate random number within specified range."""
    return random.randint(1,2)#this is set to a small set of integers for testing

def input_guess():
    """Prompts user to input text as their guess for the answer."""
    print('Guess a number:')
    return int(input())

def compute_response(guess, answer):
    """Computes response for incorrect guess."""
    if guess > answer:
        print('Too high, duuude.')
    elif guess < answer:
        print('Too low, yo.')

def correct_answer(guess, answer):
    """Computes response for correct answer."""
    if guess == answer:
        print('Correct! You are a winner!')
    #return guess == answer

answer = generate_answer()
guess = input_guess()
while guess != answer:
    compute_response(guess, answer)
    guess = input_guess()
correct_answer(guess, answer)
