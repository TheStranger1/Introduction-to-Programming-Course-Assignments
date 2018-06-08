def removeDuplicates(n):
    #found=False
    myList=[]
    for i in range(0,len(n)):
        if (not n[i] in myList ): #add only the non repeating numbers to new list
            myList.append(n[i])

    return myList



            
        
