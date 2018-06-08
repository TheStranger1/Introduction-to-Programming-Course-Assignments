def minMaxAvg(dictionary):
    minimum = min(dictionary.values())
    maximum = max(dictionary.values())
    summ = sum(dictionary.values())
    length = float (len(dictionary))
    average = (summ/length)

    tup = (minimum,maximum,average)
    tup1 = tuple(tup)
    return tup1

    
