def parseIntegers(mixedList):
    myList = []
    for item in mixedList:
        if isinstance(item,int):
            myList.append(item)
    return myList
        
