#pig latin translator

# THIS ONLY WORkS ON ONE WORD 

print('This is a pig latin translator.')
print('Type a word and hit enter to see the translation')

initial_input = input()


letter = (initial_input[0])
new_letters = letter + 'ay'
final_word = (initial_input[1 : ] + new_letters)

print(final_word)
