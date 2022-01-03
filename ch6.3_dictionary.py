#exercise 6-7
people = {
        'amy': {
            'first_name': 'amy',
             'last_name': 'smith',
             'age': '28',
             'city': 'seattle',
             },
        'bob': {
            'first_name': 'bob',
             'last_name': 'gump',
             'age': '53',
             'city': 'sanfransisco',
            },
        'george': {
            'first_name': 'george',
             'last_name': 'louise',
             'age': '37',
             'city': 'washington',
             }
        }
for person, info in people.items():
    print('\nHere is ' + person.title() + ':')
    # for infok, infov in info.items():
    #     print('\t' + infok.title() + ' is ' + infov.title() + '.')
    name = info['first_name'] + ' ' + info['last_name']
    print(name.title() + ', aged ' + info['age'] + ', lives in ' + info['city'].title())
