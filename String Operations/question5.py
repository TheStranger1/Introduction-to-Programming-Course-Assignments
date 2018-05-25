#Write a program, that queries the user for two strings, and proceeds to replace all occurrences of the
#second string in the first string with their uppercase versions; this modified string is finally output.



firstString = raw_input ("Give the fisrt string: ")
secondString = raw_input ("Give the second string: " )
stringInUpperCase = secondString.upper()
replacedString = firstString.replace(secondString, stringInUpperCase)
print "Replaced string: ", replacedString
