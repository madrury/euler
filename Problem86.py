#  A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
#  fly, F, sits in the opposite corner. By travelling on the surfaces of the room
#  the shortest "straight line" distance from S to F is 10 and the path is shown
#  on the diagram.
# 
#  However, there are up to three "shortest" path candidates for any given cuboid
#  and the shortest route doesn't always have integer length.
# 
#  By considering all cuboid rooms with integer dimensions, up to a maximum size
#  of M by M by M, there are exactly 2060 cuboids for which the shortest route has
#  integer length when M=100, and this is the least value of M for which the
#  number of solutions first exceeds two thousand; the number of solutions is 1975
#  when M=99.
# 
#  Find the least value of M such that the number of solutions first exceeds one
#  million.

# Generate a nice big set of perfect squares.
max_root = 100000 
squares = set(x**2 for x in range(max_root + 1))

def num_shortest_integer_paths(longest_side):
    '''Count the number of shortest integer paths for cuboids whose longest side
    is fixed.
    '''
    return sum((longest_side**2 + (i + j)**2) in squares
	       for i in range(1, longest_side + 1)
               for j in range(1, i+1)
           )

print "--- Testing ---"
print "Should print 1975:"
print sum(num_shortest_integer_paths(n) for n in range(1, 100))
print "Should print 2060:"
print sum(num_shortest_integer_paths(n) for n in range(1, 101))
print


# Solve the problem
# NOTE: This could be done much more efficiently by generating all the primitive
# pythagorean triples, then splitting the smaller of a, b into two summands, but
# this brute force approach works well enough.
i, count = 1, 0
while(True):
    if i%100 == 0: print "Current at side ", i
    count += num_shortest_integer_paths(i)
    if count >= 10**6:
        print "The count exceeds 10**6 for M = ", i
	break
    i += 1
