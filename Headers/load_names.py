def load_names():

    print("Loading names...")

    filename = "Resources/names.txt"

    try:
        openfile = open(filename, 'r')

    except OSError:
        print("ERROR: Cannot open",filename)
        exit() # quit program due to error

    names = []

    i = 0
    for line in openfile:
        line = line.strip()
        names.append(line)
        i += 1

    openfile.close()
    print("Load complete. Loaded",i,"names.\n")

    return names