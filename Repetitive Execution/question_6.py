#A prime number is a number that has exactly two natural number (number > 0) divisors: one and the
#number itself. Hence, the ten smallest prime numbers are 1, 2, 3, 5, 7, 11, 13, 17, 19 and 23.
#Write a program that queries the user for a number and proceeds to output whether the number is a prime
#number or not.

num = input("Enter a number: ")

if num > 0:
    for i in range (2,num):
        if (num % i) == 0:
            print str(num) + " is not a prime number"
            break


    else:
        print str(num) + " is a prime number"
        
            


else:
    print str(num) + " is not a prime number"

