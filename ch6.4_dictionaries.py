#exercise 6-9

favorite_places = {
	'sarah': ['iceland', 'norway', 'sweeden'],
	'john': ['thiland', 'baley', 'vietnam'],
	'cathy': ['auckland', 'sydney', 'canada']
	}

for person, places in favorite_places.items():
	print('\n'+ person.title() + "'s dreamlands are:")
	for i in range(3):
		print('\t' + places[i].title())
	