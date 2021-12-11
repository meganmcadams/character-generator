from Headers.load_spells import *
from Headers.load_origins import *
from Headers.load_classes import *
from Headers.split_spells import *
from Headers.load_names import *
from Headers.load_boons_banes import *
from Headers.load_races import *
from Headers.generate import *

# main
spells = load_spells()
origins = load_origins()
classes = load_classes()
class_spells = split_spells(spells, classes)
names = load_names()
boons, banes = load_boons_banes()
races = load_races()
character = generate(spells, classes, origins, boons, banes, races, names)