sandwich_orders = ['fish', 'pastrami', 'chicken', 'pastrami', 'beef', 'pastrami']
finished_sandwiches = []
print('The deli has run out of pastrami.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Your " + sandwich + " sandwich is ready.")
    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)