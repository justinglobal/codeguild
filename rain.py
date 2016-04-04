#this program reads a text weather report from a web page and returns data about it

import urllib.request
with urllib.request.urlopen(
    'https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain') as full_text:
    coded_full_text = full_text.readlines()
    #code below makes a new list of decoded list items
    raw_full_text = [data_line.decode('utf-8') for data_line in coded_full_text]

def remove_header(raw_full_text):
    """Remove first header from data"""
    return raw_full_text[12: ]#should be [12: ], to the end, use 22 for testing

def make_str_rain_data(raw_rain_data):
    """Formats raw_rain_data for processing into two items and removing bad chars
    and hour totals"""
    return [ x[0:17] for x in raw_rain_data]

def remove_spaces(str_rain_data):
    """Removes spaces from str using .split() and removes '-' using .replace()"""
    # return [ pair_str.split() for pair_str in str_rain_data]
    return [ pair_str.replace(' -' , '0').split() for pair_str in str_rain_data]
#ask david if this is the best place to use replace
def make_date_rain_dict(date_rain_pairs):
    """Make a dict from date_rain_pairs and cast the value as integer and does a unit conversion to inches """
    return { pair[0]: (.01 * int(pair[1])) for pair in date_rain_pairs}
#wtf numbers...after adding .01 * to (.01 * int(pair[1])) numbers are jacked
def get_date_max_rain(date_rain_dict):
    """Finds date with highest rain total"""
    return (max(date_rain_dict, key=date_rain_dict.get))
def get_date_max_rain_ammount(date_rain_dict):
    """"Finds and converts to inches the integer of rainfall total on date with most rain"""
    return (max(date_rain_dict.values()))

def make_rain_date_only(str_rain_data):
    """Makes a list of only the date from str_rain_data"""
    return ( [x[0: 11] for x in str_rain_data])
def make_year_rain_dict(rain_date_only, date_rain_dict):
    """Makes a dict of k:year v:total rainfall from rain_date_only & date_rain_dict"""
#CLEAN UP THE CODE BELOW IN THIS FUNCTION DEF?
    year_rain_dict = {}
    for date in rain_date_only:
        year_rain_dict[date[-4:]] = 0
    for date, total in date_rain_dict.items():
        year_rain_dict[date[-4:]] += total
    return year_rain_dict
def calc_year_max_rain(year_rain_dict):
    """Calculates year with highest rain total in year_rain_dict"""
    return (max(year_rain_dict, key=year_rain_dict.get))
def get_year_max_rain_ammount(year_rain_dict):
    """Gets integer & converts to inches for total amount of rain in year"""
    return (max(year_rain_dict.values()))

def make_daymonth_only(str_rain_data):
    """Makes a list of only the day and month from str_rain_data"""
    return ([daymonth[0: 6] for daymonth in str_rain_data])
def make_daymonth_rain_dict(daymonth_only, date_rain_dict):
    """Makes a dict of k:day/month v:total rainfall from daymonth_only & date_rain_dict"""
    daymonth_rain_dict = {}
    for daymonth in daymonth_only:
        daymonth_rain_dict[daymonth] = 0
    for daymonth, total in date_rain_dict.items():
        daymonth_rain_dict[daymonth[0: 6]] += total
    return daymonth_rain_dict

def make_daymonth_count_dict(date_rain_dict):
    """Makes a dict from the DD-MMM (daymonth) and counts the number of entries to make average"""
    daymonth_count_dict = {}
    for fulldate, count in date_rain_dict.items():
        daymonth = fulldate[:6]
        if daymonth not in daymonth_count_dict:
            daymonth_count_dict[daymonth] = []
        daymonth_count_dict[daymonth].append(count)
    return daymonth_count_dict

def get_max_any_year(daymonth_rain_dict):
    """Gets the date of any year with the highest total rainfal"""
    return (max(daymonth_rain_dict, key=daymonth_rain_dict.get))

def get_max_any_year_ammount(daymonth_rain_dict):
    """Gets the ammount for the date of any year with the highest total rainfall"""
    return (max(daymonth_rain_dict.values()))

def get_req_date():
    """"Gets a date from user (DD-MM-YYYY) to display rain total for that day"""
    print ('Enter date for rain total of that day - use DD-MMM-YYYY with month all caps & # for day and year')
    return input()

def calc_ammont_display(req_date):
    """Finds the total in inches for the day user input (DD-MM-YYYY)"""
    return (date_rain_dict[req_date])

def get_prediction_date():
    """"Gets a date from user to predict weather based on past averages"""
    print ("Input a date for weather forecast. Use DD-MMM with MMM in all caps and a # for DD.")
    return input()

def get_prediction_rain(daymonth_count_dict, prediction_date):
    """Gets a prediction for the input day/month based on averages from all data"""
    return ( (sum(daymonth_count_dict[prediction_date])) / (len(daymonth_count_dict[prediction_date])) )

raw_rain_data = remove_header(raw_full_text)
str_rain_data = make_str_rain_data(raw_rain_data)
date_rain_pairs = remove_spaces(str_rain_data)
date_rain_dict = make_date_rain_dict(date_rain_pairs)

date_max_rain = get_date_max_rain(date_rain_dict)
date_max_rain_ammount = get_date_max_rain_ammount(date_rain_dict)

rain_date_only = make_rain_date_only(str_rain_data)
year_rain_dict = make_year_rain_dict(rain_date_only, date_rain_dict)
year_max_rain = calc_year_max_rain(year_rain_dict)
year_max_rain_ammount = get_year_max_rain_ammount(year_rain_dict)

daymonth_only = make_daymonth_only(str_rain_data)
daymonth_rain_dict = make_daymonth_rain_dict(daymonth_only, date_rain_dict)
daymonth_count_dict = make_daymonth_count_dict(date_rain_dict)

max_any_year = get_max_any_year(daymonth_rain_dict)
max_any_year_ammount = get_max_any_year_ammount(daymonth_rain_dict)

print ('From 12-FEB-2002 to present day the date with the highest rainfall total is' , date_max_rain , 'with' , date_max_rain_ammount , 'inches' )
print ('The year with the highest total rainfall is' , year_max_rain , 'with' , year_max_rain_ammount , 'inches')
print ('The day of any year with the highest total rainfall is:' , max_any_year , 'with' , max_any_year_ammount , 'inches of rain')

req_date = get_req_date()
ammount_display = calc_ammont_display(req_date)
print ('Rain total for' , req_date , 'is' , ammount_display , 'inches.')

prediction_date = get_prediction_date()
prediction_rain = get_prediction_rain(daymonth_count_dict, prediction_date)
print ('The forecast for' , prediction_date , 'is' , prediction_rain , 'inches of rain.')

if prediction_rain == 0:
    print ('Enjoy the weather.')
elif prediction_date == ('20-APR'):
    print ('The forecast for 4/20 is always niiiiice.')
else:
    print ('Might want to bring a raincoat.')
