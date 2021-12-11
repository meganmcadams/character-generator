def load_objects(name):

    print("Loading origins...")

    filename = "Resources/" + name + ".txt"
    # example: "Resources/" + origins + ".txt" = "Resources/origins.txt"

    try:
        openfile = open(filename, 'r')

    except OSError:
        print("ERROR: Cannot open",filename)
        exit() # quit program due to error

    returns = []

    i = 0
    for line in openfile:
        line = line.strip()

        returns.append(line)
        i += 1

    openfile.close()

    if i < 2:
        print("ERROR: Only loaded",i,name,". Please make at least 2 options.")
        exit()

    print("Load complete. Loaded",i,name,"\n")

    return returns