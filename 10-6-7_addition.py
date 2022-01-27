from tkinter import Y


def input_num():
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
