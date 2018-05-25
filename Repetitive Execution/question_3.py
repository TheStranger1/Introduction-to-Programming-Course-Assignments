#Write a program that queries the user for a number N, and the proceeds to output all powers of two
#smaller than N. For example, if N is given a value 9, numbers 1, 2, 4 and 8 are output (20
#, 21,22 and 23).

n=int(input("Enter a number:"))

for i in range(0,n):
    if n>2**i:
        print (2**i)
    else:
        break
    
    
    
    
    
