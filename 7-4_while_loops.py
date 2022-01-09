prompt = '\nWhat toppings would you like? '
prompt += '\n(Type quit to close input.)'
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print('The following topping is added: ' + message)