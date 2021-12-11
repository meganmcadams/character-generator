def load_races():

    print("Loading races...")

    filename = "Resources/races.txt"

    try:
        openfile = open(filename, 'r')

    except OSError:
        print("ERROR: Cannot open",filename)
        exit() # quit program due to error

    races = []

    i = 0
    for line in openfile:
        line = line.strip()
        line = line.split('\t')

        races.append(line)
        i += 1

    openfile.close()
    print("Load complete. Loaded",i,"races.\n")

    return races