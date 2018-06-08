from fractions import Fraction
m = [Fraction(1,2), Fraction(1,4), Fraction(1,3)]
sum = 0
avg = 0
for i in m:
    sum+=i
    avg = (sum/len(m))

print avg
