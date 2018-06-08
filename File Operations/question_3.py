def rowAverageSum():
    file = open("matrix.txt","r")
    total = 0
    count = 0
    avglist = []
    for line in file:
        y = line.split()
        for item in y:
            total = total + int(item)
            count = count + 1
        avg = total/count
        avglist.append(avg)
    totalavg = sum(avglist)
    print avglist
    print totalavg
rowAverageSum()
