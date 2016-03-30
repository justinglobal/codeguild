# this is a weather predictor program, the user inputs a number of days and
#the program returns very accurate weather for each day

#this is the pre-refactored version:
# import random
#
# print('This is an extremely accurate weather predictor.')
# print('How many days for your very accurate weather report?')
# days_to_generate = int(input())
#
# while days_to_generate > 0:
#     day_temp = random.randint(32, 100)
#     if day_temp > 90:
#         forecast = 'Hot!'
#     elif day_temp > 60:
#         forecast = 'Nice'
#     else :
#         forecast = 'Cold!'
#     print(forecast)
#     days_to_generate -= 1

import random
#Define
def program_intro():
    """Prints introduction text for user."""
    print ('This is an extremely accurate weather predictor.')
def generate_day_temp():
    """Generates random day temperature integers."""
    return random.randint(32, 100)
def input_number_days():
    """Prompts user to input a number of days"""
    print('How many days for your very accurate weather report?')
    return int(input())
def compute_forecast(day_temp):
    """Computes forecast."""
    if day_temp > 90:
        forecast = 'Hot!'
    elif day_temp > 60:
        forecast = 'Nice'
    else :
        forecast = 'Cold!'
    return forecast
def print_forecast(forecast):
    """Prints forecast"""
    print(forecast)
#Initialize
program_intro()
#Input
number_days = input_number_days()

while number_days > 0:#Initialize
    day_temp = generate_day_temp()
    #Transform
    forecast = compute_forecast(day_temp)
    #Output
    print_forecast(forecast)
    number_days -= 1

print('Thank you for using this program.')
