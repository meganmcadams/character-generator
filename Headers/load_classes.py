def load_classes():

    print("Loading origins...")

    filename = "Resources/classes.txt"

    try:
        openfile = open(filename, 'r')

    except OSError:
        print("ERROR: Cannot open",filename)
        exit() # quit program due to error

    classes = []

    i = 0
    for line in openfile:
        line = line.strip()

        classes.append(line)
        i += 1

    openfile.close()
    print("Load complete. Loaded",i,"classes.\n")
    return classes