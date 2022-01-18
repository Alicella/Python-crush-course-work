def show_magicians(names):
    """prints the name of each magician in the list """
    for name in names:
        print(name.title())


def make_great(names, gnames):
    """add great in front of names"""
    while names:
        name = names.pop()
        gnames.append("great " + name)
    return gnames
