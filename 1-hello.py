#this program receives user input and prints a response

#pre-refactoring code:

# print('What is your name?')
# name = input()
#
# greeting = 'So nice to meet you, ' + name
# print(greeting)

def get_name():
    """Prompt user to input name text and store that name as variable"""
    print('What is your name?')
    return input()

name = get_name()

print('So nice to meet you, ' + name)
