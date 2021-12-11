def print_char(character):
    print("Generated Character")
    print("Name:",character['name'])
    print("Race:",character['race'])
    print("Origin:",character['origin'])
    print("Gender:",character['gender'])
    print("Age:",character['age'])
    print("Class:",character['class'])
    print("Boon:",character['boon'])
    print("Bane:",character['bane'])
    
    if len(character['spells']) is 0:
        print("Spells: None")

    else:
        print("Spells: ",end="")
        spells = []
        for s in character['spells']:
            spells.append(s[0])
        i = 0
        for s in spells:
            print(spells[i],end="")
            if i < len(spells) - 1:
                print(", ",end="")
            i += 1

