# this game plays Farkle, or at least a basic version of Farkle
# it uses 5 6-sided dice for each 'roll'

# User types 'roll' or hits enter to roll dice
print('This is a simple Farkle game. Press enter to roll dice.')
input()
print('Results: ')

import random

total_score = 0

dice1 = random.randint(1 , 6)
dice2 = random.randint(1 , 6)
dice3 = random.randint(1 , 6)
dice4 = random.randint(1 , 6)
dice5 = random.randint(1 , 6)

all_dice = [dice1 , dice2 , dice3 , dice4 , dice5]

#all_dice = [random.randint(1 , 6) , random.randint(1 , 6) , random.randint(1 , 6) , random.randint(1 , 6) , random.randint(1 , 6)]
#all_dice = [1, 1, 1, 1, 1]
#can make this shorter
#how to count values in a string or list
#all_dice_string = str(all_dice)

number_of_1s = all_dice.count(1)
number_of_2s = all_dice.count(2)
number_of_3s = all_dice.count(3)
number_of_4s = all_dice.count(4)
number_of_5s = all_dice.count(5)
number_of_6s = all_dice.count(6)

if number_of_1s == 3:
    total_score = total_score + 1000
#fix one scoring error here
if number_of_2s == 3:
    total_score = total_score + 200
if number_of_3s == 3:
    total_score = total_score + 300
if number_of_4s == 3:
    total_score = total_score + 400
if number_of_5s == 3:
    total_score = total_score + 500
#fix 5 scoring error here
if number_of_6s == 3:
    total_score = total_score + 600

if number_of_1s < 3:
    total_score = total_score + (number_of_1s * 100)
if number_of_5s < 3:
    total_score = total_score + (number_of_5s * 50)

#[, start[, end]]

#print('results for each dice' , all_dice)
print('results for each dice' , dice1 , dice2 , dice3 , dice4 , dice5)
print(all_dice)
print(all_dice_string)
if total_score > 0:
    print('Your total score is ' , total_score)
else:
    print('FARKLE!')

#
# num_6sided_dice = 5#int(input())
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
