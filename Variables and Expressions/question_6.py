
#Write a program that queries the user for values a, b and c and solves the roots of a quadratic
#equation

#Note, that the two roots have to be calculated separately.


from math import sqrt

#The given equation is ax^2 + bx +c = 0

a = input ("Input the value of a: ")
b = input ("Input the value of b: ")
c = input ("Input the value of c: ")

#The next lines represent root of the equation ax^2 + bx +c = 0
root1 = ( -b + sqrt(b**2 - 4*a*c)) /2*a
root2 = ( -b - sqrt(b**2 - 4*a*c)) /2*a
print root1
print root2


