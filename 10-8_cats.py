# filename1 = 'cats.txt'
# with open(filename1, 'w') as fobj:
#     fobj.write('a, b, c')

# filename2 = 'dogs.txt'
# with open(filename2, 'w') as fobj:
#     fobj.write('d, e, f')

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    try:
        with open(filename) as fobj:
            content = fobj.read()
    except FileNotFoundError:
        # print("sorry file not found")
        pass
    else:
        print(content)
