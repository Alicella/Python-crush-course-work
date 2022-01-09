while True:
    age = input("\nWhat's your age? (enter quit to stop)")
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age >= 3 and age <= 12:
            price = 10
        else:
            price = 15
        print("Ticket is $" + str(price))
