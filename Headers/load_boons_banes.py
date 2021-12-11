def load_boons_banes():

    print("Loading boons and banes...")

    # boons
    filename = "Resources/boons.txt"

    try:
        openfile = open(filename, 'r')

    except OSError:
        print("ERROR: Cannot open",filename)
        exit() # quit program due to error

    boons = []

    i = 0
    for line in openfile:
        line = line.strip()
        line = line.split('\t')

        boons.append(line)
        i += 1

    openfile.close()

    # banes
    filename = "Resources/banes.txt"

    try:
        openfile = open(filename, 'r')

    except OSError:
        print("ERROR: Cannot open",filename)
        exit() # quit program due to error

    banes = []

    j = 0
    for line in openfile:
        line = line.strip()
        line = line.split('\t')

        boons.append(line)
        j += 1

    openfile.close()

    print("Load complete. Loaded",i,"boons and",j,"banes.\n")

    return boons, banes