#Write a program that queries the user for number, and proceeds to output whether the number is an even
#or an odd number. Program terminates, when the user enters a zero.


number = input("Enter a number or a zero to quit: ")
mod = number % 2


while number >= 0:
    if (number == 0):
        print "BYE"
        break
    if (mod == 0):
        print "That's an even number"
        break
    if (mod > 0):
        print "That's an odd number"
        break
    
        


            
    


