import json


def call_num():
    filename = input('Which file to open? ')
    try:
        with open(filename) as f_obj:
            favnum = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favnum


def store_num():
    number = input('favourite number?')
    filename = input('Which file to store? ')
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)


def print_num():
    favnum = call_num()
    if favnum:
        print("Your favourite number is " + favnum)
    else:
        store_num()


print_num()
