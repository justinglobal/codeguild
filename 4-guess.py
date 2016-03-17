# import random
#
# secret = random.randint(1, 100)
#
# guess = 0
#
# while guess != secret:
#     print('guess a number')
#     guess = int(input())
#
#     if guess < secret:
#         print('Too low.')
#     elif gues > secret:
#         print('Too high.')
#     else:
#         print('Correct')




import random

secret_number = random.randint(1, 100)

# use variable 'numberofguesses' and set it to 3 to start

print('This is a guessing game')
print('Guess a number:')

guess = int(input())

while guess != secret_number:
# use and above with 'while'

    if guess > secret_number:
        print('Too high, dude.')

    elif guess < secret_number:
        print('Too low, yo.')

    print('Guess again:')
    guess = int(input())

if guess == secret_number:
    print('Correct! You are a winner!')
