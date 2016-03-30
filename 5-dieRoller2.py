#this is a simple die rolling game_intro

# this is the pre-refactored code
# import random
#
# print('This is a dice program. It will roll the number of dice you specify and tell you the average of the total results')
# print('Please input number of 6 sided dice ')
# num_6sided_dice = int(input())
# total_dice = num_6sided_dice
# total_sum = 0
#
# while 0 < num_6sided_dice:
#     dice = random.randint(1, 6)
#     total_sum += dice
#     print(num_6sided_dice, 'dice left to roll, and the value is:' , dice)
#     num_6sided_dice -= 1
#
# print('The average of all die rolls is ', int(total_sum / total_dice))

import random
def get_number_dice():
    """Gets number of dice user wants to roll."""
    print('Please input number of 6 sided dice:')
    return int(input())
def get_roll_value():
    """assigns random value which defines dice roll value"""
    return random.randint(1 , 6)
def get_average(total_sum, total_dice):
    """Computes average of die roll values"""
    return int(total_sum / total_dice)
#initialize
num_6sided_dice = get_number_dice()
total_dice = num_6sided_dice
total_sum = 0
while 0 < num_6sided_dice:
    dice = get_roll_value()#Input
    total_sum += dice#Transform
    print(num_6sided_dice , 'dice left to roll, and the value is:' , dice)#output
    num_6sided_dice -= 1
average = get_average(total_sum, total_dice)#Transform
print('The average of all die rolls is:', average)#output
