import random

print('This is a dice program. It will roll the number of dice you specify and tell you the average of the total results')
print('Please input number of 6 sided dice ')
num_6sided_dice = int(input())
total_dice = num_6sided_dice
total_sum = 0

while 0 < num_6sided_dice:
    dice = random.randint(1, 6)
    total_sum += dice
    print(num_6sided_dice, 'dice left to roll, and the value is:' , dice)
    num_6sided_dice -= 1

print('The average of all die rolls is ', int(total_sum / total_dice))
