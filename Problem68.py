from itertools import permutations, chain

def magic_3_ring():
    S = set([1, 2, 3, 4, 5, 6])
    for a_0, a_1, a_2 in permutations(S, 3):
        b_0 = b_1 = b_2 = c_0 = c_1 = c_2 = None
        s = a_0 + a_1 + a_2
	b_1 = a_2
	for b_0 in S - set([a_0, a_1, a_2]):
	    b_2 = c_1 = s - b_1 - b_0
	    if b_2 in S - set([a_0, a_1, a_2]) and b_2 != b_0:
		for c_0 in S - set([a_0, a_1, a_2, b_0, b_1, b_2]):
		    c_2 = s - c_1 - c_0
		    if c_2 == a_1 and a_0 < b_0 and a_0 < c_0:
		        yield (a_0, a_1, a_2, b_0, b_1, b_2, c_0, c_1, c_2)

def magic_5_ring():
    S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    for A in permutations(S, 3):
        A = list(A)
        B, C, D, E = [None]*3, [None]*3, [None]*3, [None]*3
	s = sum(A)
	B[1] = A[2]
	for b_0 in S - set(A):
	    B[0] = b_0
	    B[2] = C[1] = s - B[1] - B[0]
	    if B[2] in S - set(A) and B[2] != B[0]:
	        for c_0 in S - (set(A) | set(B)):
		    C[0] = c_0
		    C[2] = D[1] = s - C[1] - C[0]
		    if C[2] in S - (set(A) | set(B)) and C[2] != C[0]:
		        for d_0 in S - (set(A) | set(B) | set(C)):
			    D[0] = d_0
			    D[2] = E[1] =  s - D[0] - D[1]
			    if D[2] in S - (set(A) | set(B) | set(C)) and D[2] != D[0]:
			        for e_0 in S - (set(A) | set(B) | set(C) | set(D)):
				    E[0] = e_0
				    E[2] = s - E[1] - E[0]
				    if E[2] == A[1] and E[2] != E[0] and A[0] < B[0] and A[0] < C[0] and A[0] < D[0] and A[0] < E[0]:
				        yield (A, B, C, D, E)


for ring in magic_5_ring():
    print int("".join([str(i) for i in list(chain.from_iterable(ring))])) 
