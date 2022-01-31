import json

number = input('favourite number?')

filename = 'favnum.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
