def parsecomment():
    file = open("average.py","r")
    mylist = []
    for line in file:
        if ("#") in line:
            mylist.append(line.strip())
    file.close()
    return mylist
print parsecomment()
