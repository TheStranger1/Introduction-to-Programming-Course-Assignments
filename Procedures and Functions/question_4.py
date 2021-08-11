def lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

#This program stores two number in a and b respectively. These numbers are passed to the lcm() function. The function returns the L.C.M of two numbers.

#In the function, we first determine the greater of the two numbers since the L.C.M. can only be greater than or equal to the largest number. 
#We then use an infinite while loop to go from that number and beyond.

#In each iteration, we check if both the numbers perfectly divide our number. 
#If so, we store the number as L.C.M. and break from the loop. Otherwise, the number is incremented by 1 and the loop continues.

#The above program is slower to run. 
#We can make it more efficient by using the fact that the product of two numbers is equal to the product of the least common multiple and greatest common divisor of those two numbers.


print lcm(4, 6)
print lcm(5, 10)


# Using GCD

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))
