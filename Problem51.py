'''
By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes 
among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
 being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part
of an eight prime value family.
'''
from PrimeUtilities import makePrimeList, isPrime
primes = makePrimeList(1000000)
print "Made prime list."
primesSet = set(primes)
print "Made prime set."

def replStars(num, filter, n):
	'''In : replStars(12345, "**##*", 9)
	   Out: 99349
	'''
	S = str(num)
	N = len(S)
	return sum([10**(N - i - 1)*(n if filter[i] == "*" else int(S[i])) 
	           for i in range(len(S))])
	
def retFilters(num):
	'''In : retFilters(12211313)
	   Out: ['*##**#*#', '#**#####', '#####*#*']
	'''
	filt = []
	S = str(num)
	for i in "0123456789":
		strCnt = 0
		F = ""
		for char in S:
			if  char == i:
				F = F + "*"
				strCnt += 1
			else:
				F = F + "#"
		if strCnt >= 2:
			filt.append(F)
	return filt

def checkPrime(N):
	return (N in primesSet)

alreadySeen = set([])
for prime in primes:
	# Keep track of the primes weve already seen
	if prime > 9999 and prime not in alreadySeen:
		# Get the filters applicable to this prime
		applFilters = retFilters(prime)
		for filt in applFilters:
			# Use the filter to replace the digits with all possibilities
			digReplace = [replStars(prime, filt, i) for i in range(10)]
			# Filter down to just the primes
			newPrimes = [N for N in digReplace if checkPrime(N)]
			# Log those primes as already seen
			for p in newPrimes:
				alreadySeen.add(p)
			if len(newPrimes) >= 7:
				print newPrimes
	
		
		
	


