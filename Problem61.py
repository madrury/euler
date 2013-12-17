def genInts():
	i = 1
	while True:
		yield i
		i += 1

def genTriangles():
	'''Returns a set of all the triangular numbers with four digits.'''
	while True:
		for n in genInts():
			T = n*(n+1) // 2
			if T > 9999:
				raise StopIteration
			if T > 999:
				yield str(T)
			
def genSquares():
	'''Returns a set of all the triangular numbers with four digits.'''
	while True:
		for n in genInts():
			T = n*n
			if T > 9999:
				raise StopIteration
			if T > 999:
				yield str(T)
				
def genPentagonals():
	'''Returns a set of all the triangular numbers with four digits.'''
	while True:
		for n in genInts():
			T = n*(3*n - 1) // 2
			if T > 9999:
				raise StopIteration
			if T > 999:
				yield str(T)
				
def genHexagonals():
	'''Returns a set of all the triangular numbers with four digits.'''
	while True:
		for n in genInts():
			T = n*(2*n - 1)
			if T > 9999:
				raise StopIteration
			if T > 999:
				yield str(T)
				
def genHeptagonals():
	'''Returns a set of all the triangular numbers with four digits.'''
	while True:
		for n in genInts():
			T = n*(5*n - 3) // 2
			if T > 9999:
				raise StopIteration
			if T > 999:
				yield str(T)
				
def genOctagonals():
	'''Returns a set of all the triangular numbers with four digits.'''
	while True:
		for n in genInts():
			T = n*(3*n - 2)
			if T > 9999:
				raise StopIteration
			if T > 999:
				yield str(T)
				
from StringUtilities import rearrangements
				
G = {'T': list(genTriangles()),
	 'S': list(genSquares()),
	 'P': list(genPentagonals()),
	 'X': list(genHexagonals()),
	 'H': list(genHeptagonals()),
	 'O': list(genOctagonals())}
	 
print G['T']
print G['S']
print G['P']
	 
S = 'TSPXHO'
R = rearrangements(S)
R = [x for x in R if x[0] == 'T']
print R

for searchSpace in R:
	print 'Searching: ', searchSpace
	for N1 in G[searchSpace[0]]:
		for N2 in G[searchSpace[1]]:
			if N1[2:4] == N2[0:2]:
				for N3 in G[searchSpace[2]]:
					if N2[2:4] == N3[0:2]:
						for N4 in G[searchSpace[3]]:
							if N3[2:4] == N4[0:2]:
								for N5 in G[searchSpace[4]]:
									if N4[2:4] == N5[0:2]:
										for N6 in G[searchSpace[5]]:
											if N5[2:4] == N6[0:2] and N6[2:4] == N1[0:2]:
												print "Matched :", (N1, N2, N3, N4, N5, N6)
												print "The sum is: ", int(N1) + int(N2) + int(N3) + int(N4) + int(N5) + int(N6)
			






