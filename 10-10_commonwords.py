filename = 'gutenberg.txt'

with open(filename) as fobj:
    lines = fobj.readlines()

i = 0
for line in lines:
    i += line.lower().count('the')

print(i)
