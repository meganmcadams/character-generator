from random import randrange

def generate(spells, classes, origins, boons, banes, races, names, class_spells):

    print("Generating character...")

    # character
    character = {}

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
    character['class'] = classes[randrange(0,(len(classes) - 1))]
    character['origin'] = origins[randrange(0,(len(origins) - 1))]
    character['race'] = races[randrange(0,(len(races) - 1))]
    character['boon'] = boons[randrange(0,(len(boons) - 1))]
    character['bane'] = banes[randrange(0,(len(banes) - 1))]
    character['level'] = randrange(0,20)
    
    # age
    rand_num = randrange(0,5)
    ages = ['Child','Teen','Young Adult','Adult','Elder Adult','Elder']
    character['age'] = ages[rand_num]

    # spells
    character['spells'] = []
    pos_num = len(class_spells[(character['class'])])
    if pos_num > 20:
        pos_num = 20
    if pos_num < 2:
        character['spells'] = class_spells[(character['class'])]
    else:
        num = randrange(0,pos_num - 2) + 1
        chos_num = []

        i = 0
        while i < num:
            rand_num = randrange(0,pos_num)

            if rand_num not in chos_num:
                chos_num.append(rand_num)
                character['spells'].append(class_spells[(character['class'])][rand_num])

            i += 1

    print("Character generated.\n")

    return character