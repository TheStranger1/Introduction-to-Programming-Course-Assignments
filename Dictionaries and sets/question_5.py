def vowelProportions(string):
    counta=int(string.count("a") / len(string) * 10)
    counte=int(string.count("e") / len(string) * 100)
    counti=int(string.count("i") / len(string) * 100)
    counto=int(string.count("o") / len(string) * 100)
    countu=int(string.count("u") / len(string) * 100)
    county=int(string.count("y") / len(string) * 100)
    dict={}
    

    keys=['a','e','i','o','u','y']
    values=[counta,counte,counti,counto,countu,county]
    for i in range(0,len(keys)):
        key=keys[i]
        value=values[i]
        dict[key]=value
    return dict
#print (vowelProportions("aaccfedubbbyyyy"))
            
        
        
