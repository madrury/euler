# It is well known that if the square root of a natural number is not an integer,
# then it is irrational. The decimal expansion of such square roots is infinite
# without any repeating pattern at all.
# 
# The square root of two is 1.41421356237309504880..., and the digital sum of the
# first one hundred decimal digits is 475.
# 
# For the first one hundred natural numbers, find the total of the digital sums of
# the first one hundred decimal digits for all the irrational square roots.
from decimal import * # <-- Filthy cheating!
getcontext().prec = 102

def digital_sum(n):
    rt = Decimal(n)**Decimal(.5)
    digits = str(rt).replace('.', '')
    return sum(int(d) for d in digits[0:100])

print "--- Testing, should print 475 ---"
print digital_sum(2)

squares = {x**2 for x in range(1, 10)}
print "--- The answer is: ---"
print sum(digital_sum(n) for n in range(1, 100) if n not in squares)
