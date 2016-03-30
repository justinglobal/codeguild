#this program reads a text weather report from a web page and returns data about it

import urllib.request
with urllib.request.urlopen(
    'http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain') as full_text:
    coded_full_text = full_text.readlines()
    #code below makes a new list of decoded list items
    raw_full_text = [data_line.decode('utf-8') for data_line in coded_full_text]

def remove_header(raw_full_text):
    """Remove first header from data"""
    return raw_full_text[12: 22]#should be [12: ], to the end, use 22 for testing

def make_str_rain_data(raw_rain_data):
    """Formats raw_rain_data for processing into two items and removing bad chars
    and hour totals"""
    return [ x[0:17] for x in raw_rain_data]

def remove_spaces(str_rain_data):
    """Removes spaces from str using .split() """
    return [ pair_str.split() for pair_str in str_rain_data]

def make_date_rain_dict(date_rain_pairs):
    """Make a dict from date_rain_pairs and case the value as integer """
    return { pair[0]: int(pair[1]) for pair in date_rain_pairs}

def get_date_max_rain(date_rain_dict):
    """Finds date with highest rain total"""
    return (max(date_rain_dict, key=date_rain_dict.get))
def get_date_max_rain_ammount(date_rain_dict):
    """"Finds and converts to inches the integer of rainfall total on date with most rain"""
    return (.01 * (max(date_rain_dict.values())))


raw_rain_data = remove_header(raw_full_text)
str_rain_data = make_str_rain_data(raw_rain_data)
date_rain_pairs = remove_spaces(str_rain_data)
date_rain_dict = make_date_rain_dict(date_rain_pairs)

date_max_rain = get_date_max_rain(date_rain_dict)
date_max_rain_ammount = get_date_max_rain_ammount(date_rain_dict)


#below code removes everything but year and rain total from  final_rain_data
year_rain_only = ( [x[7:17] for x in str_rain_data])
#below code splits year_rain_only to remove spaces
year_rain_pairs = [ year_pair_tosplit.split() for year_pair_tosplit in year_rain_only]
#below code makes a dictionary of the year_rain_pairs and makes the value an int
year_rain_dict = { year_pair[0]: int(year_pair[1]) for year_pair in year_rain_pairs}
year_rain_tup = tuple(year_rain_pairs)
#below code finds total rainfall for each year, or maybe max as well
# max_year_rain_total = (sum(year_rain_dict.values()))

# (max(sum(year_rain_dict, key=year_rain_dict.get)))

# matthew's solution
# def create_year_to_rain_total_dict(day_month_year_list, ranfall_dict):
#     yeart_to_rainfall_total_dict = {}
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
# print (year_rain_only)
# print (year_rain_pairs)
# print (year_rain_dict)
# print (year_rain_tup)

# print (max_year_rain_total)






print ('From 12-FEB-2002 to present day the date with the highest rainfall total is' , date_max_rain , 'with' , date_max_rain_ammount , 'inches' )
# #code below gets date from user
# print ('Enter date for rain total of that day - use DD-MMM-YYYY with month all caps & # for day and year')
# req_date = input()
# #code below converts req_date from 1/100th of an inch into inches for display
# date_display = (.01 * date_rain_dict[req_date])
#
# print ('Rain total for' , req_date , 'is' , date_display , 'inches.')


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
