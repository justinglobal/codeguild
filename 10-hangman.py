

# secret words: python, django, concatenate

import random

def choose_secret_word():
    """Chooses a secret word from a list."""
    # return random.choice(['python' , 'django' , 'concatenate'])
    return random.choice(['concatenate' , 'concatenate' , 'concatenate'])
secret_word = choose_secret_word()
print (secret_word)

def make_display_word(secret_word):
    """Makes an initial set of underscores for every letter in secret_word"""
    return ('_ ' * len(secret_word))
display_word = make_display_word(secret_word)
print (display_word)

def get_guess():
    """Asks user to input a letter"""
    print('Choose a letter:')
    return input()
guess = get_guess()

def find_letters_not_display(guess, secret_word):
    """Finds the letters not to display to user, if they guess correctly"""
    return set(secret_word) - set(guess)
letters_not_display = find_letters_not_display(guess, secret_word)
print (letters_not_display)

letters_not_display_list = list(letters_not_display)
print (letters_not_display_list)

secret_word_list = list(secret_word)
print (secret_word_list)

new_display_word = []
#use an if statement instead of a for loop
for letters_not_display_list in secret_word_list:
    new_display_word = secret_word_list.insert(len(secret_word_list, '_')
    # new_display_word = secret_word_list.insert([0: ], '_')

print(new_display_word)

print (secret_word_list)#(list(secret_word))

print (letters_not_display_list)#(list(letters_not_display))

# print('Welcome to this Hangman Game! Press enter to play:')
# input()
# print ('Choose a letter:')
# print (display_word)
# print

# split.generate_word into list of each character word_letters
#
# remaining_mistakes = 6
# current_word() = list of underscore
# update_used_letters()
# update_current_word()
# update_remaining_mistakes()
#
# print current_word
# print remaining_mistakes
#
#
#
# input() = guess
#
# if guess in word_letters
#     update_current_word
#     print current_word
#     print used_letters
#     print remaining_mistakes
#
# if guess not in word_letters
#     update_used_letters
#     update_remaining_mistakes
#     print current_word
#     print used_letters
#     print remaining_mistakes
#
# find_letters()
# remove_letter()
#
# use replace
#
# str.replace(old, new[, count])
# can use .index on string, but only can find first
#
# set can compare and remove keep track of guesses
#
# use list() to make string into list
#
# only need to keep track of secret_word and list of guessed numbers
