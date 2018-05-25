#A parity bit is a bit which is added into beginning of a bit pattern to find transmission errors, so that the
#resulting pattern has an odd number of ones. Hence, if the original pattern has an odd number of ones, the
#parity bit added is a zero; if the original pattern has an even number of ones, the parity bit added is a one.
#Write a program that queries the user for a bit pattern and outputs the bit pattern with parity bit added.


bitPattern = raw_input ("Give a bit pattern: ")
numberOfOnes = bitPattern.count ("1")


mod = numberOfOnes % 2


if mod > 0:
    print "parity bit added: " + str (0) + bitPattern

if mod == 0:
    print "parity bit added: " + str (1) + bitPattern
