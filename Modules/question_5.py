import random


def generateGroup(sizeOfGroup):
    myFile = open("persons.dat", "r")   #opens file for reading
    namesList = []
    randomList = []
    for line in myFile:
        a = line.split(",")
        namesList.append(a[0])          #appends the names only into a list

    while len(randomList) < sizeOfGroup:
        y = random.choice(namesList)    #select unique randon names
        if y not in randomList:
            randomList.append(y)



    myFile.close()                      #closes file

    return randomList

    

group = generateGroup(12)

print (group)



