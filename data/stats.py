from shared import *

all_abs = allAbs()
print('total # of pokemons:', len(all_abs))
ids = [a.id for a in all_abs]
print('total # of unique ids:', len(set(ids)))
print('max id:', max(ids))
print('total # of unique names:', len(set(a.name for a in all_abs)))
