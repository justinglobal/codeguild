#pig latin translator

print('This is a pig latin translator.')
print('Type a word and hit enter to see the translation')

initial_input = input()
#receives word or sequence of words
word_list = initial_input.split()
#splits string into list of each word in sequence

final_words = []

##srt.lower()

for root in word_list:
    letter = (root[0])
    word_body = (root[1 : ])
    final_letters = letter +'ay'
    final_words.append(word_body + final_letters)
    #final_word = word_body + final_letters
    # new_letters = letter + 'ay'
    # final_word = (initial_input[1 : ] + new_letters)
    ##print(letter)
#print(final_word)

final_output = ' '.join(final_words)

print(final_output)
#print(final_words)
#print(word_list)
##print(letter)


# ages = [32, 16, 22]
#
# new_ages = []
#
# for age in ages:
#         updated_age = age +1
#         new_ages.append(updated_age)
#
# print(new_ages)
