city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

print (city_to_accessible_cities)

print (city_to_accessible_cities['Albany'] & city_to_accessible_cities['Portland'])

#all_cities = ['Boston', 'Portland', 'New York', 'Philadelphia', 'Albany']

#print (all_cities)

#city_visited = (city_to_a

#all_cities - 
