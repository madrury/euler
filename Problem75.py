from collections import Counter
transformations = {'L1': lambda a, b, c: (a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c),
                   'L2': lambda a, b, c: (a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c),
		   'L3': lambda a, b, c: (-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c)}

max_perim = 1500000

#triples = set([])
perimiters = Counter()

def recurse_triples(triple):
    global triples
    perim = sum(triple)
    if perim < max_perim:
        # triple is primitive, add all the multiples that keep us below the permiter
        s = max_perim / perim
	for p in range(perim, max_perim + 1, perim):
	    perimiters[p] += 1
	#triples |= set((k*triple[0], k*triple[1], k*triple[2]) for k in range(1, s+1))
	# Recurse down the tree
	recurse_triples(transformations['L1'](*triple))
	recurse_triples(transformations['L2'](*triple))
	recurse_triples(transformations['L3'](*triple))

recurse_triples((3, 4, 5))

print sum(perimiters[x] == 1 for x in perimiters)
