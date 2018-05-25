#Write a program that queries the user for two 4-character strings, and proceeds to test and output whether
#the first string contains all letters of the second string in reverse order.

firstString = raw_input ("Give the 1st string: ")
secondString = raw_input ("Give the 2nd string: ")

firstStringInReverse = firstString [::-1]


if secondString ==  firstStringInReverse:
    print firstString + " IS " + secondString + " in reverse order"

else:
    print firstString + " is not " + secondString + " in reverse order"
