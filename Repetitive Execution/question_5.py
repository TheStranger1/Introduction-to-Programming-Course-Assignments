#String B is said to be a permutation of string A, if an equal amount of each character in A can be found in B
#and vice versa. Hence, B is said to be a rearrangement of A. For example, strings “ABBA”, “BAAB” and
#“ABAB” are all permutations of string “AABB”, and string “elvis” and “sevil” are permutations of string
#“lives”. Note, that these string permutations are sometimes called anagrams.
#Write a program that queries the user for strings A and B, and proceeds to output whether B is a
#permutation of A. To confirm this, the following conditions need to be met:
#1. There is an equal amount of characters in A and B (or, the length of A is equal to length of B), and
#2. For every character found in A, there is an equal amount of same character in B

stringa=raw_input("Enter string A: ") 
stringb=raw_input("Enter string B: ")

perm=False #boolean variable initially set to false.

for char in stringa: 
    if char in stringb and set(stringa)==set(stringb): #check if for every character in stringa is present in #string b and if the length of both is equal
        perm=True #set perm to true if the condition is met
while(perm):
    print stringb,"is a permutation of",stringa 
    break
