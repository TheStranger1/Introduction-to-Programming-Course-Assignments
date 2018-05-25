#Write a program that queries the user for a string containing a DNA sequence, and proceeds to output the
#proportions of four nucleotide bases (A, C, G and T) as percentage values. You can assume that the user
#enters the sequence in lower case. If the user enters an empty string, display an error message.


dnaSequence = raw_input ("Enter sequence: ")

lengthOfSequence = len(dnaSequence)


countA = float (dnaSequence.count ("a"))
countT = float (dnaSequence.count ("t"))
countC = float (dnaSequence.count ("c"))
countG = float (dnaSequence.count ("g"))



proportionOfA = int ((countA/lengthOfSequence) * 100)
proportionOfT = int ((countT/lengthOfSequence) * 100)
proportionOfC = int ((countC/lengthOfSequence) * 100)
proportionOfG = int ((countG/lengthOfSequence) * 100)

if lengthOfSequence == 0:
    print "ERROR"

else:
    print "Proportion of A: " + str (proportionOfA) + " percent"
    print "Proportion of T: " + str (proportionOfT) + " percent"
    print "Proportion of C: " + str (proportionOfC) + " percent"
    print "Proportion of G: " + str (proportionOfG) + " percent"


    
    


    


    
