#this is a simple (sort of) madlib game

#this is the pre refactored version
# print('This is a madlib game.')
# print(' What is your favorite color')
# color = input()
# print('What is your preferred mode of transportation?')
# transport = input()
# print('What is your favorite holiday?')
# holiday = input()
# print('You will receive a ' + color + ' ' + transport + ' on ' + holiday)

#this is the refactored version

def game_intro():
    """prints text to introduce game to user"""
    print('This is a madlib game.')

def get_color():
    """asks user for to enter text of their favorite color"""
    print('What is your favorite color?')
    return input()

def get_transport():
    """asks user to enter text of their favorite mode of transport"""
    print('What is your preferred mode of transportation?')
    return input()

def get_holiday():
    """asks user to enter text of their favorite holiday"""
    print('What is your favorite holiday?')
    return input()

def compute_output(color, transport, holiday):
    """computes and prints output of user entered text"""
    return ('You will receive a ' + color + ' ' + transport + ' ' + 'on' + ' ' + holiday)

game_intro()

color = get_color()
transport = get_transport()
holiday = get_holiday()

madlib = compute_output(color, transport, holiday)

print(madlib)
