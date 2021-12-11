from Headers.load_spells import *
from Headers.load_origins import *
from Headers.load_classes import *
from Headers.split_spells import *
from Headers.load_names import *
from Headers.load_boons_banes import *

# main
spells = load_spells()
origins = load_origins()
classes = load_classes()
class_spells = split_spells(spells, classes)
names = load_names()
boons, banes = load_boons_banes()