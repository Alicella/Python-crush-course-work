from collections import OrderedDict

people = OrderedDict()
people['alice'] = 26
people['bob'] = 50
people['giovani'] = 30
people['emily'] = 13

for person, age in people.items():
    print(person.title() + ' is ' + str(age) + ' years old.')
