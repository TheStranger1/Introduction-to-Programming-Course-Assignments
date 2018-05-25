#Write a program that queries the user for a 4-bit binary string and decodes it into decimal number.

binary = raw_input ("Give a 4-bit binary string: ")
lengthOfBinary = len(binary)
decimal = int (binary, 2)


if lengthOfBinary == 4:
    print str(binary)+ " is " + str(decimal) + " as decimal number"

else:
    print "Error"
    
                
