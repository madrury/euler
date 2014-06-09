# There exactly fourteen triangles containing a right angle that can be formed when
# each co-ordinate lies between 0 and 2 inclusive; that is, 0  x1, y1, x2, y2  2.
# 
# Given that 0  x1, y1, x2, y2  50, how many right triangles can be formed?
from math import floor

def gcd(a, b):
    '''We need this!'''
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b  
    return a 

# We count by splitting the collection of all such triangles into four disjoint
# groups.

# Type 1:
#   These trinagles have thier right angle at the (0, 0) coordinate.  Each such
# triangle is determined by a point along the x-axis and a point along the
# y-axis niether of which is (0, 0)
def count_type_1(nx, ny):
    return (nx-1)*(ny-1)

# Type 2:
#  These triangles have thier right angle abutting the x axis, i.e. one of thier
# sides is perpendicular to the x-axis.  Each of these triangles has one point
# along the x-axis and one point along the same vertical line.  There are as
# many of these as type 1 triangles.

# Type 3:
#  Same as type 2, but the right angle abutts on the y axis.  There are as many
#  of these as type 2.

# Type 4:
#  This is the meat of the counting problem, these are niether type 1, 2, or 3
# so the right angle is in the interior of the reigon, at some point (x, y).  To
# count these, we note that that the interior side must be perpendicular to the
# vector (x, y), i.e. parallel to (y, -x).  That is, we need to find the count
# of rational numbers p/q such that p/q * (y, -x) has integer coordinates
# satifying the feasability conditions:
#     x + p/q * y  <= nx
#     y - p/q * x  >= 0
# To avoid double counting we enforce p/q > 0 and then repeat using (-y, x).
#
# To solve this, just note that q must divide both x and y, so we simply let
# q = gcd(x, y), then count how many p can work by solving the feasability
# conditions explicitly.
def count_type_4(nx, ny, x, y):
    g = gcd(x, y)
    n_right = min(floor( (((nx-1) - x)*g)/float(y) ),
                  floor( (y*g)/float(x) )
	      )
    n_left = min(floor( (((ny-1) - y)*g)/float(x) ),
                 floor( (x*g)/float(y) )
	      )
    return n_right + n_left

# So here's the solution
def count_all(nx, ny, verbose = False):
    type_1 = count_type_1(nx, ny)
    type_4 = sum(count_type_4(nx, ny, x, y) 
                 for x in range(1, nx)
		 for y in range(1, ny)
	     )
    return 3*type_1 + type_4

# Run the count
print "--- Total number of triangles: ---"
print count_all(51, 51)
