filename = 'guestbook.txt'

with open(filename, 'a') as file_object:
    while True:
        username = input("What's your name? ")
        print('Hello, ' + username.title())
        file_object.write(username.title() + ' just visited.\n')
