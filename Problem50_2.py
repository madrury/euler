'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

def longestSum(upBound):
	
	from PrimeUtilities import makePrimeList
	primeList = makePrimeList(upBound)
	print primeList
	
	bestSum = 2
	bestLen = 1
	
	primeCnt = -1
	for startPrime in primeList:
		if startPrime * bestLen > upBound:
			break
		primeCnt += 1
		# Make the list to take the summands from
		currList = primeList[primeCnt:]
#		print "currList ", currList
		# Length of the current sum
		currLen = 0
		currSum = 0
		for sumPrime in currList:
			# Increment the sums
			currSum += sumPrime
			currLen += 1
#			print "currSum ", currSum, "currLen ", currLen
			# If we've overshot, break out of the inner loop
			if currSum > upBound:
#				print "Break"
				break
			if currSum in primeList and currLen > bestLen:
				bestSum = currSum
				bestLen = currLen
#				print "bestSum ", bestSum, "bestLen ", bestLen

	print bestSum, bestLen
		
			
longestSum(1000000)
