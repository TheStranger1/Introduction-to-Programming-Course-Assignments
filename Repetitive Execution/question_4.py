#Write a program that queries the user for a string, and proceeds to generate a new string with all of the
#letters from the original string that are in upper case. This generated string is then output. You can assume
#that the string given does not contain characters other than letters (e.g. numbers or spaces).

string=raw_input("Enter a string: ")
newString=""
for char in string:
    if char>='A'and char<='Z':#Check for capital letters in string
        newString=char #add the uppercase letters to the empty string in each iteration
        print newString 
