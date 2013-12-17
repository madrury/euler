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
	numPrimes = len(primeList)
	# Initialize the longest sum
	bestPrime = 2
	bestSumList = [2]
	bestSumLen = 1
	# Loop over primes to start the prime at 
	for strtIndex in range(10):
		# Initialize the sum
		currSum = primeList[strtIndex]
		# Initialize the index for the sum
		sumIndex = strtIndex
		# Initialize the list of primes being summed
		sumList = [currSum]
		sumLen = 1
		while currSum <= upBound and sumIndex < numPrimes:
			# Check if we sum to a prime, and have a better solution than before
			if currSum in primeList and sumLen > bestSumLen:
				bestPrime = currSum
				bestSumList = sumList
				bestSumLen = sumLen
			# Increment everything
			sumIndex += 1
			try:
				sumList.append(primeList[sumIndex])
				currSum += primeList[sumIndex]
				sumLen += 1
			except:
				pass
		# Print what weve got:
		# Increment the index where we start summing
		strtIndex += 1
	# Print out the result
	print 'Start index %i , longest sum %s , giving prime %i :' % (strtIndex, str(bestSumList), bestPrime)	
			
longestSum(1000000)
