def split_spells(spells, classes):

    print("Splitting spells into classes...")

    class_spells = {}

    for c in classes:
        class_spells[c] = []

    for s in spells:
        split = s[2].split(',')
        for item in split:
            class_spells[item].append(s)

    print("Splitting complete.")

    return class_spells