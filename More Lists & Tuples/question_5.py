def getTaller(listOfPeople,height):
    
    lst=[]
    for person in listOfPeople:
        if person[1]>height:
            lst.append(person)
    return lst


person1 = ("John", 170, 69)
person2 = ("James", 180, 79)
person3 = ("Lisa", 163, 57)
person4 = ("Anne", 174, 55)
person5 = ("Peter", 195, 101)
personList = [ person1, person2, person3, person4, person5 ]
tallerList = getTaller(personList, 175)
print tallerList
        

