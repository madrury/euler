# Each of the six faces on a cube has a different digit (0 to 9) written on it;
# the same is done to a second cube. By placing the two cubes side-by-side in
# different positions we can form a variety of 2-digit numbers.
# 
# For example, the square number 64 could be formed:
# 
# In fact, by carefully choosing the digits on both cubes it is possible to
# display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49,
# 64, and 81.
# 
# For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
# one cube and {1, 2, 3, 4, 8, 9} on the other cube.
# 
# However, for this problem we shall allow the 6 or 9 to be turned upside-down so
# that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for
# all nine square numbers to be displayed; otherwise it would be impossible to
# obtain 09.
# 
# In determining a distinct arrangement we are interested in the digits on each
# cube, not the order.
# 
# {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5} 
# {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
# 
# But because we are allowing 6 and 9 to be reversed, the two distinct sets in the
# last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the
# purpose of forming 2-digit numbers.
# 
# How many distinct arrangements of the two cubes allow for all of the square
# numbers to be displayed?

# There are C(9, 6) = 84 different arrangements for a single die.  So a double
# loop brute force method is feasable.  Note that there is no possibility for
# the dice to match, so we can overcount then divide by 2.  We also echew the
# digit 9, cause it is interchangeable with 6.
#
# Let's go...

def represents(n, die_1, die_2):
    dig_1 = n / 10
    dig_2 = n % 10
    return ((dig_1 in die_1 and dig_2 in die_2) or
            (dig_1 in die_2 and dig_2 in die_1)
	   )

def test_it(die_1, die_2):
    #both = die_1 | die_2
    #if len(both) < 7:
    #    return False
    return (represents(1, die_1, die_2) and
            represents(4, die_1, die_2) and
            represents(6, die_1, die_2) and
            represents(16, die_1, die_2) and
            represents(25, die_1, die_2) and
            represents(36, die_1, die_2) and
            represents(46, die_1, die_2) and
            represents(64, die_1, die_2) and
            represents(81, die_1, die_2)
	   )

print "--- Testing ---"
print "Should print true: ", test_it(set([0, 5, 6, 7, 8, 6]),
                                     set([1, 2, 3, 4, 8, 6])
			     )

# Solve the problem
from itertools import combinations

digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

count = 0
for d1 in combinations(digits, 6):
    for d2 in combinations(digits, 6):
        d1, d2 = set(d1), set(d2)
	if 9 in d1:
	    d1.remove(9); d1.add(6)
	if 9 in d2:
	    d2.remove(9); d2.add(6)
        count += test_it(d1, d2)

print "The number of ordered solutons is: ", count
print "The number of unordered solutions is ", count / 2
