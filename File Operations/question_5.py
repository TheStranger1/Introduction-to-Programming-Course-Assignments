def parsePersons():
    myFile = open("persons.txt", "r")
    myDict={}
    
    
    for line in myFile:
        y = line.split(",")
        x = (int(y[1]),int(y[2]),int(y[3]))
        z = y[0]
        myDict[z] = x
    print myDict

parsePersons()
        
