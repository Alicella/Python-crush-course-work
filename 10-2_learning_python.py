filename = 'learn_python.txt'

with open(filename) as file_object:
    # opt 1
    contents = file_object.read()
    print(contents.rstrip())

    # opt 2
    for line in file_object:
        print(line.replace('you', 'I').rstrip())

    # opt 3
    lines = file_object.readlines()

for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.rstrip())
