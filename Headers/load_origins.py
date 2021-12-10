def load_origins():

    print("Loading origins...")

    filename = "Resources/origins.txt"

    try:
        openfile = open(filename, 'r')

    except OSError:
        print("ERROR: Cannot open",filename)
        exit() # quit program due to error

    origins = []

    i = 0
    for line in openfile:
        line = line.strip()
        line = line.split('\t')

        origins.append(line)
        i += 1

    openfile.close()
    print("Load complete. Loaded",i,"origins.\n")

    return origins