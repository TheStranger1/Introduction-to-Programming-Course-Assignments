#Write a program that queries the user for three numbers and outputs the smallest of them

firstNumber = input ("Give the 1st number: ")
secondNumber = input ("Give the 2nd number: ")
thirdNumber = input ("Give the 3rd number: ")

if firstNumber < secondNumber and firstNumber < thirdNumber:
    print firstNumber, "is the smallest"


