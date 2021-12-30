people = []
people.append('Amy')
people.append('Brian')
people.append('Charles')
message = ', welcome to dinner!'
# Brian can't make it
people[1] = 'David'

# More people to invite
people.insert(0, 'Emily')
people.insert(2, 'Fred')
people.append('Green')

# big table unavailable
popped_person = people.pop()
sorry = ', sorry you cannot come.'
print(popped_person + sorry)
popped_person = people.pop()
sorry = ', sorry you cannot come.'
print(popped_person + sorry)
popped_person = people.pop()
sorry = ', sorry you cannot come.'
print(popped_person + sorry)
popped_person = people.pop()
sorry = ', sorry you cannot come.'
print(popped_person + sorry)

print(people[0] + message)
print(people[1] + message)

del people[1]
del people[0]
print(people)
