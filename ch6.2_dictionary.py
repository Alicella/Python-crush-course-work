favorite_languages = { 'jen': 'python',
'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

people = ['edward', 'dexter', 'jen', 'phil', 'ashley']

print('Here are the participants: ')
print(sorted(favorite_languages.keys()))
print('\nHere is the poll: ')
print(set((favorite_languages.values())))

for person in people:
	if person in favorite_languages.keys():
		print('\n' + person.title() + ', thanks for taking the poll.')
	else:
		print('\n' + person.title() + ', welcome to take the poll!')
