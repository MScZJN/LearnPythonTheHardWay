cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."

# ok pay attention!


while True:
	print "State? (ENTER to quit)",
	state = raw_input("> ")

	if not state: break

	# this line is the most impotant ever! study!
	city_found = find_city(cities, state)
	print city_found