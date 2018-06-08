def sortList(tupleList):
    return tupleList[0] * tupleList[1]
    

myList = [(2, 3.0), (3, 1.0), (4, 2.5), (1, 1.0)]
#print sortList(myList)
print sorted(myList,key = sortList)
    #tupleList.sort(key=lambda tup: tup[0]*tup[1])
