# option_1
# import functions_module as fm

# names = ['brian', 'chandler', 'janice']
# gnames = []

# gnames = fm.make_great(names, gnames)
# fm.show_magicians(gnames)

# option_2
from functions_module import make_great as makeg
from functions_module import show_magicians as showm

names = ['brian', 'chandler', 'janice']
gnames = []

gnames = makeg(names[:], gnames)
showm(gnames)
showm(names)
