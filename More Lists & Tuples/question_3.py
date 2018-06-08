def capitalizeName(nameAgeTuple):
    
    #return nameAgeTuple[0][0].upper()+nameAgeTuple[0][1:],nameAgeTuple[1]
    return nameAgeTuple[0].title(),nameAgeTuple[1]
    
test = ("john copperfield", 32)
print capitalizeName(test)
