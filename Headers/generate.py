from random import randrange

def generate(spells, classes, origins, boons, banes, races, names):

    print("Generating character...")

    # character
    character = {}
    character_items = ['stats','gender','origin','boon','bane']

    # stats
    stats = {}
    stats_names = ['strength','constitution','dexterity','intelligence','wisdom','charisma']

    for stat in stats_names:
        stats[stat] = (randrange(1,17) + 3)
    
    character['stats'] = stats

    # gender
    genders = ['Male','Female','Nonbinary']
    character['gender'] = genders[randrange(0,2)]

    # name
    character['name'] = names[randrange(0,(len(names) - 1))] + " " + names[randrange(0,(len(names) - 1))]

    # other
    character['origin'] = origins[randrange(0,(len(origins) - 1))]
    character['race'] = races[randrange(0,(len(races) - 1))]
    character['boon'] = boons[randrange(0,(len(boons) - 1))]
    character['bane'] = banes[randrange(0,(len(banes) - 1))]

    return character, character_items