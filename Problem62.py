from PrimeUtilities import isCube
from StringUtilities import rearrangements
from collections import defaultdict
		
K = defaultdict(int)
KK = defaultdict(list)
for i in range(10000):
	C = i**3
	S = ''.join(sorted(str(C)))
	K[S] += 1
	KK[S].append(i**3)
	
for S in K:
	if K[S] == 5:
		print min(KK[S])
	