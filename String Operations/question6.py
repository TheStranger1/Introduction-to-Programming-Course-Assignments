#Write a program that queries the user for strings A and B. The program then proceeds to find the index of
#the second occurrence of string B in string A.


stringA = raw_input ("Give the string A: ")
stringB = raw_input ("Give the string B: ")


location = stringA.find (stringB, 1)

print "The index of the 2nd occurrence of B in A is ", location


