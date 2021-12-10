def load_spells():
    
    print("Loading spells...")

    headers = ["Spell Name","Level","Class(es)","School","Casting Time","Range",
    "Target/Area","Component(s)","Concentration","Duration",
    "Attack/Saving Throw (Effect)","DAM Type","Damage/Heal","Additional Detail"]

    # get class info

    filename = "Resources/spells.txt"

    try:
        openfile = open(filename, 'r')

    except OSError:
        print("ERROR: Cannot open",filename)
        exit() # quit program due to error

    headers_done = False
    spells = []

    i = 0
    for line in openfile:
        line = line.strip()
        line = line.split('\t')

        if headers_done is False:
            headers_done = True
            for item in line:
                if item not in headers:
                    print("ERROR:",item,"not found in hardcoded headers")
                    
        else:
            spells.append(line) # record spell
            i += 1

    openfile.close() # close the file
    print("Load complete. Loaded",i,"spells.\n")

    return spells