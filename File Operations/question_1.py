file = open("products.txt", "w")
s = ""

while(True):
    pname = raw_input("Enter product name: ")
    if pname=="":
        print "Bye"
        break
    
    pprice = input("Enter the price: ")
    s+=str(pname)+","+str(pprice)+"\n"
    file.flush()
    file.write(s)
 


file.close()
    
    
