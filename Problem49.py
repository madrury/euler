from StringUtilities import rearrangements
from PrimeUtilities import *

checked = []
primes = makePrimeList(10000)

for num in range(1000, 10000):

	strNum = str(num)
	strArr = rearrangements(strNum)
	numArr = [int(S) for S in strArr]
	for N in numArr:
		if N > num:
			diff = N - num
			lastTerm = N + diff
			if str(lastTerm) in strArr and all([num in primes, N in primes, lastTerm in primes]):
				print num, N, lastTerm