# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by moving left, right, up, and down, is indicated in bold red and
# is equal to 2297.

test_matrix = [
 [131, 673, 234, 103, 18],
 [201, 96, 342, 965, 150],
 [630, 803, 746, 422, 111],
 [537, 699, 497, 121, 956],
 [805, 732, 524, 37, 331]
]
# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
# As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the
# bottom right by moving left, right, up, and down.

# A solution using Dykstra's algorithm.

def iter_nbrs(entry, n_row, n_col):
    '''An iterator over the adjacent entries of a matrix.'''
    return ((entry[0] - i, entry[1] - j) for i in set([-1, 0, 1])
                                         for j in set([-1, 0, 1])
              if i == 0 or j == 0          and 
	         0 <= entry[0] - i < n_row and
	         0 <= entry[1] - j < n_col and
		 (i, j) != entry
           )

def nbrs(entry, n_row, n_col):
    return set(x for x in iter_nbrs(entry, n_row, n_col))

def init_distances(init_entry, n_row, n_col):
    dists = [
                [float("inf") for j in range(n_col)]
	        for i in range(n_row)
	    ]
    i0, j0 = init_entry
    dists[i0][j0] = 0
    return dists

def init_unvisited(n_row, n_col):
    return {(i, j) for i in range(n_row)
	           for j in range(n_col)
	   }

def update_current(unvisited, dist_matrix):
    new_current, best_val = (0, 0), float("inf")
    for p in unvisited:
        d = dist_matrix[p[0]][p[1]]
        if d < best_val:
	    new_current, best_val = p, d
    return new_current
    
#-----------------------------------------------------------------------------
filenm = 'matrix_problem_83.txt'
with open(filenm, 'rb') as f:
    matrix = []
    for line in f:
        row = [int(x) for x in line.split(',')]
	matrix.append(row)

this_matrix = matrix
n_row, n_col = len(matrix), len(matrix)

init_entry = (0, 0)
dest_entry = (n_row-1, n_col-1)

# Initialize everything important
dist_matrix = init_distances(init_entry, n_row, n_col)
unvisited = init_unvisited(n_row, n_col)
visited = set([])
current = init_entry

# Run the algorithm until the shortest path between the two nodes is found
while(True): 
    unvisited_nbrs = unvisited & nbrs(current, n_row, n_col)
    for nbr in unvisited_nbrs:
        new_dist = min(
	    this_matrix[nbr[0]][nbr[1]] + dist_matrix[current[0]][current[1]],
	    dist_matrix[nbr[0]][nbr[1]]
	)
	dist_matrix[nbr[0]][nbr[1]] = new_dist
    visited.add(current)
    unvisited.remove(current)
    current = update_current(unvisited, dist_matrix)
    # Break condition
    if dest_entry in visited:
        break

print "--- The algorithm has terminated with distance: ---"
print dist_matrix[dest_entry[0]][dest_entry[1]]
print "--- Adding on the initial node, the minimal path length is: ---"
print dist_matrix[dest_entry[0]][dest_entry[1]] + this_matrix[0][0]
