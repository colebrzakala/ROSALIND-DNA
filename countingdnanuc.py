def countDNAnuc(fname):
    file = open(fname, 'r')
    s = file.read()
    file.close()
    acount = 0
    tcount = 0
    ccount = 0
    gcount = 0
    for elem in s:
        if elem == "A":
            acount += 1
        if elem == "C":
            ccount += 1
        if elem == "G":
            gcount += 1
        if elem == "T":
            tcount += 1
    print (acount, ccount, gcount, tcount)
