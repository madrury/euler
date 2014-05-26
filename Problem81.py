# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
# right, by only moving to the right and down, is indicated in bold red and is
# equal to 2427.

test_case = [[131, 673, 234, 103, 18],
             [201, 96,  342, 965, 150], 
	     [630, 803, 746, 422, 111], 
	     [537, 699, 497, 121, 956], 
	     [805, 732, 524, 37,  331]]

# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
# As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the
# bottom right by only moving right and down.

#-------------------------------------------------------------------------------

# Read the matrix from the file
filenm = 'matrix_problem_81.txt'
with open(filenm, 'rb') as f:
    matrix = []
    for line in f:
        row = [int(x) for x in line.split(',')]
	matrix.append(row)

n_row = len(matrix)
print "We have a %s by %s matrix." % (n_row, n_row)

# Create an indexing set for the diagonals of the matrix.
# I.e., each diagonal is determined by an equation i + j = c, where i and j are 
# indexes into the matrix, we create a data structure:
#   {c: [list of (i, j) in diagonal]}

from collections import defaultdict

diagonals = defaultdict(list)
for i in range(n_row):
    for j in range(n_row):
        diagonals[i + j].append((i, j))

# Solve the problem with dynamic programming:
#  We work diagonal by diagonal, keeping track and updating the minimum path
# satisfying the constraints and ending up at teh given entry.

best_path_sums = defaultdict(int)
for c in range(0, 2*n_row - 1):
    for i, j in diagonals[c]:
        # Update the best values:
	if i == 0 and j == 0:
	    best_path_sums[(i, j)] = matrix[i][j]
	elif i == 0:
	    best_path_sums[(i, j)] = matrix[i][j] + best_path_sums[(i, j-1)]
	elif j == 0:
	    best_path_sums[(i, j)] = matrix[i][j] + best_path_sums[(i-1, j)]
	else:
	    best_path_sums[(i, j)] = min(
	        matrix[i][j] + best_path_sums[(i-1, j)],
	        matrix[i][j] + best_path_sums[(i, j-1)]
	    )

print best_path_sums[(79, 79)]
