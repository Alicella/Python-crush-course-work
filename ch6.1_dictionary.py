glossary = {'variable': 'varies', 
			'loop': 'loops', 
			'list': 'lists', 
			'float': 'floats',
			'string': 'strings'}
for k, v in glossary.items():
	print(k.title() + ': ' + v + '.')
print('\n')

del glossary['loop']
for name in glossary.keys():  #for name in glossary:
	print(name)
print('\n')
# confirm loop is deleted.

for meaning in glossary.values():
	print(meaning.upper())