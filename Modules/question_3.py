from datetime import date
def dateAfter(d1,d2):
    day1,month1,year1 = d1.split('.')
    day2,month2,year2 = d2.split('.')
    first = date(int(year1),int(month1),int(day1))
    second = date(int(year2),int(month2),int(day2))
    if first>second:
        return True
    else:
        return False
    
    
    

