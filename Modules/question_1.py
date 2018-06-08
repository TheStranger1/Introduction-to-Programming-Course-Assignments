from random import randint
num = input("Enter a number: ")
output = []

for i in range(num):
    output.append(randint(1,100))

print output
