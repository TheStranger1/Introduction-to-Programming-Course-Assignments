#Write a program that queries the user for a number N, and then proceeds to output all numbers between
#(-N and N).

n=input("Enter a number:")

for i in range(-n,n+1):
    print i
