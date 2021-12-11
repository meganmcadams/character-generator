from random import randrange

def generate(spells, classes, origins, boons, banes, races):

    print("Generating character...")

    # character
    character = {}
    character_items = ['stats','gender','origin']

    # stats
    stats = {}
    stats_names = ['strength','constitution','dexterity','intelligence','wisdom','charisma']

    for stat in stats_names:
        stats[stat] = (randrange(1,17) + 3)
    
    character['stats'] = stats

    # gender
    genders = ['Male','Female','Nonbinary']
    character['gender'] = genders[randrange(0,2)]

    # other
    character['origin'] = origins[randrange(0,(len(origins) - 1))]
    character['race'] = races[randrange(0,(len(races) - 1))]