#pig latin translator 2 works on string of words

#this is the pre refactored code
print('This is a pig latin translator.')
print('Type a word and hit enter to see the translation')

initial_input = input()
#receives word or sequence of words
word_list = initial_input.split()
#splits string into list of each word in sequence

final_words = []

for root in word_list:
    letter = (root[0])
    word_body = (root[1 : ])
    final_letters = letter +'ay'
    final_words.append(word_body + final_letters)

final_output = ' '.join(final_words)

print(final_output)
################################################################
##refactoring in process
# def get_initial_words():
#     """Prompts user to input text."""
#     print('Type a word and hit enter to see the translation:')
#     return input()
#
# def split_initial_words():
#     """Splits user input into list of each word in sequence."""
#     return initial_input.split()
#
# initial_words = get_initial_words()
# word_list = split_initial_words()
# final_words = []
