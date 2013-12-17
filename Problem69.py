from primes import sieve
from math import sqrt

def largest_prod_less_than(n):
    prod = 1
    for prime in sieve(int(sqrt(n))):
        prod *= prime
	if prod > n: return prod / prime

N = largest_prod_less_than(1000000)
print "The number is %s" % N
