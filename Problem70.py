from __future__ import division
from primes import sieve
from strings import make_histogram, is_rearrangement
from itertools import product

def close_primes(N, delta):
    '''Make a list of the primes close to the square root of N.'''
    from math import sqrt
    rt_N = int(sqrt(N))
    return [p for p in sieve(rt_N + delta + 1)
                if abs(rt_N - p) < delta]

# The delta is chosen through trial and error...
N = 10**7
test_primes = close_primes(N, 5000)

ans, phi_ratio_ans = None, None
# Check all the plausable pairs of primes
for p, q in product(test_primes, test_primes):
    n = p*q
    phi = ((p - 1)*(q - 1) if p != q else p*(p-1))
    phi_ratio = n / phi
    if (n < N and
        is_rearrangement(str(n), str(phi)) and
        ((not phi_ratio_ans) or (phi_ratio < phi_ratio_ans))):
	# Then....
        ans, phi_ratio_ans = n, phi_ratio

print 'Found: n = %s, phi ratio = %s.' % (ans, phi_ratio_ans)
