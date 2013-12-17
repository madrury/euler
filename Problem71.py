from __future__ import division
from math import floor
from operator import itemgetter

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def find_closest(q, N):
    fracs = [(floor(q[0]*m/q[1]), m) for m in xrange(2, N+1) 
                if gcd(floor(q[0]*m/q[1]), m) == 1 and 
		m != q[1]]
    vals = [frac[0]/frac[1] for frac in fracs]
    return fracs[max(enumerate(vals), key = itemgetter(1))[0]]

def find_next(qq, N):
    flr_prt = floor((N + qq[0][1])/qq[1][1])
    return ( (qq[1][0], qq[1][1]), 
             (flr_prt*qq[1][0] - qq[0][0],
              flr_prt*qq[1][1] - qq[0][1]) )

# Problem 73
# print find_closest((3, 7), 1000000)

# Problem 74
current = (find_closest((1, 3), 12000), (1, 3))
print 'Starting at: ', current
count = 0
while current[1] != (1.0, 2):
    current = find_next(current, 12000)
    count += 1

print count

