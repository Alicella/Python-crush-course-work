def input_num():
    """keep prompting the user to input an integer until they follow the instruction"""
    while True:
        m = input("Enter a number: ")
        try:
            n = int(m)
            if n is int:
                break
        except ValueError:
            msg = "Pls input an integer"
            print(msg)
        else:
            return n


x = input_num()
y = input_num()
print(x + y)
