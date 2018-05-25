#Write a program that queries the user for a two word string (i.e. a string with two words separated with a
#space), and outputs the latter word. Hint: you need to use the find() method with the [] operator.


myString = raw_input ("Enter a two word sentence: ")
spaceLocation = myString.find(" ")
secondWord = myString [spaceLocation+1:]

print "The second word is ",secondWord
