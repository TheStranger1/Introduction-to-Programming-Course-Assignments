lst=[]
while(True): #Continuously ask for a number 
    number=int(input("Enter a number or zero to quit: "))
    if (number!=0):
        lst.append(number)
    elif number==0:
        break #Break condition for the while loop
print (lst)

