import urllib
def calculateDigits():
    wpage = urllib.urlopen("http://users.utu.fi/ertaka/prog/digits.txt")
    content = wpage.read()
    return sum(int(x) for x in content if '0' <= x <= '9')
    
