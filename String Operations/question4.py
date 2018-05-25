#Write a program that queries the user for two strings, and proceeds to output the number of times the
#string can be found in another string (the output must be produced for both strings).



firstString = raw_input ("Give the first string: ")
secondString = raw_input ("Give the second string: ")

#How many times the first string can be found in the second string
location1 = secondString.count (firstString)

#How many times the second string can be found in the first string
location2 = firstString.count (secondString)

print "The first string can be found ", location1, "times in the second string"
print "The second string can be found ", location2, "times in the first string"

