def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def evenNumbers(myList):
    evens = []
    for number in myList:
        if is_even(number):
            evens.append(number)
    return evens
   
