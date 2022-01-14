polls = {}
active = True
while active:
    name = input('\nWhat is your name? ')
    response = input('If you could visit one place in the world, where would you go? ')
    polls[name]=response

    repeat = input('Anyone else to take the poll? yes/no ')
    if repeat == 'no':
        active = False
print('\nPoll results:')
for name, response in polls.items():
    print(name.title() + ' would like to go to ' + response.title() + '.')