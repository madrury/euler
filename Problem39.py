'''
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
        {20,48,52}, {24,45,51}, {30,40,50}
    For which value of p < 1000, is the number of solutions maximised?
'''

# Organize the triples here by perimeter
perimDict = dict((P, set([])) for P in range(1001))
# Let's generate pythagorean triples with the formula of euclid
# since (a + b)^2 >= a^2 + b^2 = c^2, we have P > 2c --> c < 1000/2 = 500
for m, n, k in [(i, j, k) for i in range(1, 501) for j in range(1, i + 1) for k in range(1, 2000/(i+j) + 1)]:
	# Make the pythagorean triple
	a = k*(m**2 - n**2)
	b = k*2*m*n
	c = k*(m**2 + n**2)
	P = a + b + c
	# Store the triple under it's parameter
	if P <= 1000:
	    perimDict[P].add((a, b, c))
# Derive a dicionary of couts	
countDict = dict((P, len(perimDict[P])) for P in perimDict)
# Where is the max?
M = max(countDict[P] for P in countDict)

print perimDict[120]

# Print out the data where there is a maximum number of triples
for P in perimDict:
	if countDict[P] == M:
		print P, countDict[P], perimDict[P]

	