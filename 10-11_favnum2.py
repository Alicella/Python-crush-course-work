import json

filename = 'favnum.json'
with open(filename) as f_obj:
    favnum = json.load(f_obj)
    print("Your favourite number is " + favnum)
