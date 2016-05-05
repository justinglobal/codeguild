# this demonstrates refactoring functions by defining new functions

#fist is the old code then the re-factored code

#this is the old code:
# import random
#
# secret_number = random.randint(1, 100)
# keep_guessing = True
#
# while keep_guessing:
#     print('Guess my secret number:')
#     guessed_number = int(input())
#     if guessed_number > secret_number:
#         print('Too high.')
#     elif guessed_number < secret_number:
#         print('Too low.')
#     else:
#         print('Correct!')
#         keep_guessing = False


import random

# Step 1: Define
def generate_secret_number():
    """Randomly generate an int between 1 and 100 for the user to guess. Return it."""
    return random.randint(1, 2)

def prompt_user_for_guess():
    """Ask user to enter their guess for the secret number. Return the guess as an int."""
    print('Guess my secret number:')
    return int(input())

def assess_guess(secret, guess):
    """Determine if the user's guess was too high, low, or correct. Return a string representing that."""
    if guess > secret:
        assessment = 'Too high.'
    elif guess < secret:
        assessment = 'Too low.'
    else:
        assessment = 'Correct!'
    return assessment

def should_keep_guessing(assessment):
    """Return if the program should keep prompting for guesses as a bool."""
    return assessment != 'Correct!'

# Step 2: Initialize
secret_number = generate_secret_number()
keep_guessing = True

while keep_guessing:
    # Step 3: Input
    guessed_number = prompt_user_for_guess()

    # Step 4: Transform
    assessment = assess_guess(secret_number, guessed_number)
    keep_guessing = should_keep_guessing(assessment)

    # Step 5: Output
    print(assessment)

print(should_keep_guessing.__doc__)
