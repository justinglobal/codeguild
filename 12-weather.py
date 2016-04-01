#this program reads a text weather report from a web page and returns data about it

import urllib.request
with urllib.request.urlopen(
    'http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain') as full_text:
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
#CLEAN UP THE CODE BELOW IN THIS FUNCTION DEF
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
#question: does the above code make a de-duped list? i think it does
daymonth_rain_dict = make_daymonth_rain_dict(daymonth_only, date_rain_dict)
# print ((daymonth_only)[0:20])
# print (daymonth_only.count('27-MAR'))
#
# # str.count(sub[, start[, end]])
#
# # print (daymonth_rain_dict)
#
# print ((rain_date_only)[0:20])
# print (rain_date_only.count('27-MAR'))


# this code meant well but doesn't work
# daymonth_count = for date, rain in date_rain_pairs.count()
# print (daymonth_count)

def make_daymonth_count_dict(date_rain_dict):
    """ """
    daymonth_count_dict = {}
    # for daymonth in daymonth_only:
    #     daymonth_count_dict[daymonth] = []
    for fulldate, count in date_rain_dict.items():
        daymonth = fulldate[:6]
        if daymonth not in daymonth_count_dict:
            daymonth_count_dict[daymonth] = []
        daymonth_count_dict[daymonth].append(count)
    return daymonth_count_dict

daymonth_count_dict = make_daymonth_count_dict(date_rain_dict)
# print (daymonth_count_dict)

def get_prediction_date():
    """"gets a date from user to predict weather based on past averages"""
    print ("Input a date for weather forecast. Use DD-MMM with MMM in all caps and a # for DD.")
    return input()

# below is the functional print statements for problem
#below code finds day/month with highest total rainfall
print ('The day of any year with the highest total rainfall is:' , (max(daymonth_rain_dict, key=daymonth_rain_dict.get)))
#below code find the integer total for day/month with highest total rainfall
print ('With' , (max(daymonth_rain_dict.values())) , 'inches of rain')
#below is the functional ending print statements
print ('From 12-FEB-2002 to present day the date with the highest rainfall total is' , date_max_rain , 'with' , date_max_rain_ammount , 'inches' )
print ('The year with the highest total rainfall is' , year_max_rain , 'with' , year_max_rain_ammount , 'inches')

#code below gets date from user
print ('Enter date for rain total of that day - use DD-MMM-YYYY with month all caps & # for day and year')
req_date = input()
#code below converts req_date from 1/100th of an inch into inches for display
date_display = (date_rain_dict[req_date])

print ('Rain total for' , req_date , 'is' , date_display , 'inches.')
#alternate way to print:
# for item in (top_ten):
#   print (item[0], item[1])

prediction_date = get_prediction_date()

# def find_date_rain_avg(daymonth_count_dict, prediction_date):
#
# weather = {'01-JUN': [0.11, 0.16, 0.0, 0.0], '09-MAY': [0.0, 0.16, 0.0], '03-JAN': [0.08, 0.01, 0.03, 0.0], '12-SEP': [0.0, 0.0, 0.0, 0.0], '28-FEB': [0.0, 0.01, 0.15, 0.14], '01-FEB': [0.01, 0.31, 0.08, 0.0]}
# date = '01-JUN'

print ( (sum(daymonth_count_dict[prediction_date])) / (len(daymonth_count_dict[prediction_date])) )

    # for daymonth, count in daymonth_count_dict.items():
    # (sum(daymonth_count_dict.values())) / ()



# grades = [90, 92, 98, 99, 99]
# print ((sum(grades)) / (len(grades)))

# daymonth_count_dict = {}
# for daymonth, total in date_rain_dict.items():
#
# non unique list is rain_date_only
# non unique list is daymonth_only
#
# return { pair[0]: (.01 * int(pair[1])) for pair in date_rain_pairs}

#this is some dumb example I made it means nothing
# >>> print (day_totals)
# {'12-NOV': 98, '04-OCT': 0, '21-MAY': 91, '22-SEP': 28, '08-SEP': 0, '14-MAR': 213}
# >>> print (max(day_totals))
# 22-SEP







#below code works but is not necessary, keeping it now for reference
#below code removes everything but year and rain total from str_rain_data
# year_rain_only = ( [x[7:17] for x in str_rain_data])
#below code splits year_rain_only to remove spaces
# year_rain_pairs = [ year_pair_tosplit.split() for year_pair_tosplit in year_rain_only]
#below code makes a dictionary of the year_rain_pairs and makes the value an int
# year_rain_dict = { year_pair[0]: int(year_pair[1]) for year_pair in year_rain_pairs}
#year_rain_tup = tuple(year_rain_pairs)

#below code finds total rainfall for each year, or maybe max as well
# max_year_rain_total = (sum(year_rain_dict.values()))
# (max(sum(year_rain_dict, key=year_rain_dict.get)))







# andrew's solution
# def create_year_to_rain_total_dict(day_month_year_list, ranfall_dict):
#     year_to_rainfall_total_dict = {}
#     for date in day_month_year_list:
#         year_to_rainfall_total_dict[date[-4:]] = 0
#
#     for x, y in rainfall_dict.items():
#         year_to_rainfall_total_dict[x[-4:]] += y
#     return year_to_rainfall_total_dict



#below code splits final_rain_data and removes spaces
# date_rain_pairs = [ pair_str.split() for pair_str in str_rain_data]
# #code below makes a dictionary of the pairs from code above
# date_rain_dict = { pair[0]: int(pair[1]) for pair in date_rain_pairs}

# print (str_rain_data)
# print (date_rain_pairs)
# print (date_rain_dict)
# print (rain_date_only)
# print (year_rain_only)
# print (year_rain_pairs)

# print (year_rain_tup)
# print (year_rain_dict)
# print (year_max_rain)
# print (max_year_rain_total)




#code below works but is not necessary after using dict comprehention on date_rain_pairs
# max_day_rain_total = (.01 * (int(max([ x[15:17] for x in str_rain_data]))))
# rain_date = ( [x[0: 11] for x in str_rain_data])
# day_rain_total = ([ x[15:17] for x in str_rain_data])
# day_rain_total_nospace = (str(day_rain_total).replace(' ' , ''))
# print (rain_date)
# print (day_rain_total)
# print (final_rain_data)

#two defined functions 'get_date_max_rain' and 'get_date_max_rain_ammount' above replace this code below
# #code below finds the day in dict with most rain
# max_rain_total_day = (max(date_rain_dict, key=date_rain_dict.get))
# #code below finds the ammount of rain in inches
# max_rain_total_ammount = (.01 * (max(date_rain_dict.values())))

# print ([ x[0:10] for x in final_rain_data])
# print (day_rain_total)
# print (rain_date)
# print (day_rain_total_nospace)
# print (list(day_rain_total_nospace))
# print ('The day with the most rain had:' , max_day_rain_total , 'inces of rain')
# #data is str, need integers to do operations...or could wait until end

# print (date_rain_dict)

# with urllib.request.urlopen('https://imgs.xkcd.com/comics/ballmer_peak.png') as f:
#     print(f.read(10000))

    #return ' '.join(book_lines).lower().replace('\n' , '').replace('.', '').replace(',' , '').split()
