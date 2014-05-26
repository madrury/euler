# It can be seen that a rectangular grid measuring 3 by 2 contains eighteen
# rectangles.
# 
# Although there exists no rectangular grid that contains exactly two million
# rectangles, find the area of the grid with the nearest solution.

# Simple counting principle:
#   The number of rectangles is the number of pairs of non-collinear points 
# divided by 4.
num_rect = lambda n, m: n*m*(n+1)*(m+1)/4

print "--- Test the number of rectangles --"
print "The number of rectangles in a 1*1 grid is: ", num_rect(1, 1)
print "The number of rectangles in a 1*2 grid is: ", num_rect(1, 2)
print "The number of rectangles in a 2*3 grid is: ", num_rect(2, 3)

target_num = 2*10**6

# Heuristic:
#   Note that num_rect ~ n**2 * m**2 / 4, so if we have num_rect ~ 2*10**6
# then m ~ 2 * sqrt(2) * 10**3 / n
#   On the edges of the search space num_rect ~ n**4 / 4, so if we have
# num_rect ~ 2*10**6 then n ~ 2**(1/4) * 10**(5/2)
from math import sqrt

n_bound = int(2**(1/4) * 10**(5/2)) + 1
m_bound = lambda n: int(2 * sqrt(2) * 10**3 / n) + 1

rect_counts = {}
for n in range(1, n_bound):
    for m in range(1, m_bound(n)):
       rect_counts[(n, m)] = num_rect(n, m)

# Find the entry closest to two million
two_mill = 2 * 10**6
closest, close_dist = 0, two_mill 
for k, v in rect_counts.iteritems():
    dist = abs(v - two_mill)
    if dist < close_dist:
        close_dist = dist
	closest = k

print "--- Solution ---"
print "The number of rectangles closest to two million is: "
print rect_counts[closest]
print "The dimensions of this rectangle are: "
print closest
print "The area of this rectangle is: "
print closest[0] * closest[1]
        

