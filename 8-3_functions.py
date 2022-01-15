def make_shirt(size='l', message='i love python'):
    """print a sentence summarizing the size of the shirt and the message printed on it ."""
    print("The shirt of size " + size.upper() + " says " + message.title() + '.')

# make_shirt('L', "have a good day")
# make_shirt(message='have a good day', size='xs')
make_shirt('m')
make_shirt('s', 'happy birthday')
make_shirt(message='happy birthday')