#String B is said to be a permutation of string A, if an equal amount of each character in A can be found in B
#and vice versa. Hence, B is said to be a rearrangement of A. For example, strings “ABBA”, “BAAB” and
#“ABAB” are all permutations of string “AABB”, and string “elvis” and “sevil” are permutations of string
#“lives”. Note, that these string permutations are sometimes called anagrams.
#Write a program that queries the user for strings A and B, and proceeds to output whether B is a
#permutation of A. To confirm this, the following conditions need to be met:
#1. There is an equal amount of characters in A and B (or, the length of A is equal to length of B), and
#2. For every character found in A, there is an equal amount of same character in B


stringA = input("Enter string A: ")
stringB = input("Enter String B: ")

perm = False

if set(stringA) == set(stringB) and len(stringA) == len(stringB):
    perm = True

while (perm):
    print(stringB + " is a permutation of " + stringA)
    break
