# The smallest number expressible as the sum of a prime square, prime cube, and
# prime fourth power is 28. In fact, there are exactly four numbers below fifty
# that can be expressed in such a way:
# 
#    28 = 2**2 + 2**3 + 2**4 
#    33 = 3**2 + 2**3 + 2**4 
#    49 = 5**2 + 2**3 + 2**4 
#    47 = 2**2 + 3**3 + 2**4
# 
# How many numbers below fifty million can be expressed as the sum of a prime
# square, prime cube, and prime fourth power?

# Make a list of all the primes up to sqrt(fifty_million)
from primes import sieve

fifty_million = 50 * 10**6
P = list(sieve( int( (fifty_million)**.5 ) ))

# Solve the problem, brute force and not at all clever or thoughtful
numbers = set()
for p_1 in P:
   for p_2 in P:
       n = p_1**2 + p_2**3
       if n >= fifty_million: 
           break
       for p_3 in P:
           m = n + p_3**4
	   if m >= fifty_million:
	       break
	   else:
	       numbers.add(m)

print len(numbers)
