def show_magicians(names):
    """prints the name of each magician in the list """
    for name in names:
        print(name.title())

# def make_great(names):
#     """NOT modify the list of magicians by adding the phrase the Great to each magician’s name"""
#     great_names = []
#     for name in names:
#         great_names.append("great " + name)
#     return great_names
# great_names = make_great(names)
# show_magicians(great_names)

def make_great(names, gnames):
    while names:
        name = names.pop()
        gnames.append("great " + name)
    return gnames

names = ['brian', 'chandler', 'janice']
gnames = []

gnames = make_great(names[:], gnames)
show_magicians(gnames)
show_magicians(names)