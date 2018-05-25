#Write a program that queries the user for two strings and outputs the longer one


firstString = raw_input ("Give the first string: ")

secondString = raw_input ("Give the second string: ")

firstStringLength = len(firstString)

secondStringLength = len(secondString)


if firstStringLength > secondStringLength:
    print firstString + " is longer"

if secondStringLength > firstStringLength:
    print secondString + " is longer"
     
