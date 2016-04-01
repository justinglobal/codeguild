#this program is a 'road trip' information program. user inputs a city and the
#program returns information about what city can be visited next from a dict


city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

def get_start_city():
    """Gets city input from user and shows other cities reachable from input city"""
    print ("Choose a city from the list to see all cities connected to that city.")
    print ("Choices: Boston, New York, Albany, Portland, Philadelphia")
    return input()

def make_first_hop(start_city, city_to_accessible_cities):
    """Makes list of cities connected to the input city"""
    return city_to_accessible_cities[start_city]

start_city = get_start_city()
print(make_first_hop(start_city, city_to_accessible_cities))

cities_visited = start_city
print (cities_visited)

print (start_city)

cities_not_visited =  (set(city_to_accessible_cities.keys())) - (set(start_city))
print(cities_not_visited)




# print (city_to_accessible_cities.keys())
# all_cities = (city_to_accessible_cities.keys())
# print (all_cities)
#
# print (set(city_to_accessible_cities.keys()))

# print (city_to_accessible_cities)
# d = {'cat': 4, 'snake': 0}
# d['cat']
# animal = 'cat'
# d[animal]
# d['c' + 'at']
# other_animal = 'catdog'
# d[other_animal[4:]]
# d[str.replace(other_animal, 'd' + 'og')]
#
# for x in d.keys()
# for x in set(d.keys()) - {'snake'}
#
# def return_six():
#     x = 6
#     return x
#
#     x = pow(3, 2)
#
#     y = 3
#     pow(pow(3, 1), 2)
#
#     pow(2 + pow(99, 0), 2)
#
#
#     x = 3 + 3
#     return x
#
#     return 6
#
#     return 3 + 3
#
#     return pow(3, 2)
