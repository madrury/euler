# The optimal path sum in the 5 by 5 matrix below, by starting in any cell in the
# left column and finishing in any cell in the right column, and only moving up,
# down, and right, is indicated in red and bold; the sum is equal to 994.

test_matrix = [[131, 673, 234, 103, 18],
	       [201, 96, 342, 965, 150],
	       [630, 803, 746, 422, 111],
	       [537, 699, 497, 121, 956],
	       [805, 732, 524, 37, 331]]

# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
# As...'), a 31K text file containing a 80 by 80 matrix, from the left column to
# the right column.


# The update step
def update(current_best, next_column, n_row):
    ret_vect = []
    # Loop over all the values in next_colunm, and find the minimum path 
    # value ending here
    for curr_ind in range(n_row):
        canidates = []
	canidates.extend(
	    vert_then_back_vals(current_best, next_column, curr_ind, n_row)
	)
	canidates.extend(
	    back_then_vert_vals(current_best, next_column, curr_ind, n_row)
	)
	ret_vect.append(min(canidates))
    return ret_vect
	           
def vert_then_back_vals(current_best, next_col, curr_ind, n_row):
    # Go up from the current index to position j, and then back to the 
    # current best.  Sum all of these entries.
    ret_val = []
    for j in range(n_row):
        if j < curr_ind:
	    ret_val.append(sum(next_col[j:curr_ind+1]) + 
	                   current_best[j]
	    )
	if j == curr_ind:
	    ret_val.append(current_best[curr_ind] + next_col[curr_ind])
	if j > curr_ind:
	    ret_val.append(sum(next_col[curr_ind:j+1]) +
	                   current_best[j]
            )
    return ret_val
            
print "---- Testing vert than back vals ---"
cb = [1, 2, 3]
nc = [3, 2, 1]
print "Current Best: ", cb
print "Next Column: ", nc
print "Going vertical and then backwards: ", vert_then_back_vals(cb, nc, 1, 3) 

def back_then_vert_vals(current_best, next_col, curr_ind, n_row):
    # Go back to the column of current bests, then vertiaclly to position j.
    # Sum all of these entries.
    ret_val = []
    for j in range(n_row):
        if j < curr_ind:
	    ret_val.append(next_col[curr_ind] +
	                   sum(current_best[j:curr_ind+1])
	    )
	if j == curr_ind:
	    ret_val.append(current_best[curr_ind] + next_col[curr_ind])
	if j > curr_ind:
	    ret_val.append(next_col[curr_ind] +
	                   sum(current_best[curr_ind:j+1])
	    )
    return ret_val

print "---- Testing back then vert vals ---"
cb = [1, 2, 3]
nc = [3, 2, 1]
print "Current Best: ", cb
print "Next Column: ", nc
print "Going backwards and then vertical: ", back_then_vert_vals(cb, nc, 1, 3) 

#-----------------------------------------------------------------------------
# Solve the problem with dynamic programming
#-----------------------------------------------------------------------------

# Read the matrix from the file
filenm = 'matrix_problem_81.txt'
with open(filenm, 'rb') as f:
    matrix = []
    for line in f:
        row = [int(x) for x in line.split(',')]
	matrix.append(row)

n_row = len(matrix)
print "The matrix has %s rows and %s columns" % (n_row, n_row)

# Dynamic programming

# Initialize the current best left to right sums as the first column of the 
# matrix.  This corresponds to the n_row by 1 case.
best_sums = [matrix[i][0] for i in range(n_row)]
for col in range(1, n_row):
    print best_sums
    best_sums = update(current_best = best_sums,
                       next_column = [matrix[i][col] for i in range(n_row)],
		       n_row = n_row
		)
print "--- The best final column is:"
print best_sums
print "--- The minimum path sum is:"
print min(best_sums)


