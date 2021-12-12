from Headers.load_spells import *
from Headers.load_objects import *
from Headers.split_spells import *
from Headers.generate import *
from Headers.print_char import *

# load
spells = load_spells()
classes = load_objects("classes")
class_spells = split_spells(spells, classes)
origins = load_objects("origins")
names = load_objects("names")
boons = load_objects("boons")
banes = load_objects("banes")
races = load_objects("races")
personalities = load_objects("personalities")

# generate
character = generate(spells, classes, origins, boons, banes, races, names, class_spells, personalities)

# print
print_char(character)
