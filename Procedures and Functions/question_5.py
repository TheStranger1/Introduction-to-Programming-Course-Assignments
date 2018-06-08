def rotateLeft(pattern):
    return pattern[1:]+pattern[0] #the first bit goes to the back


def rotateRight(pattern):
    return pattern[len(pattern)-1]+pattern[:len(pattern)-1]#last bit comes at first


pattern=raw_input("Enter a bit pattern: ")
direction=(raw_input("Enter the direction: "))
steps=int(input("Enter the number of steps: "))

for i in range(0,steps):
    if direction=="left":
        pattern=rotateLeft(pattern)
    else:
        pattern=rotateRight(pattern)
print ("Rotated pattern: " + str(pattern))
