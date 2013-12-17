'''
    "The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at          
     each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

     Find the sum of the only eleven primes that are both truncatable from left to right and right to left."
'''

from PrimeUtilities import makePrimeList
primeList = makePrimeList(1000000)

# Now solve the problem
ansList = []
for prime in primeList:
    strPrime = str(prime)  # String representation of the prime under constideration
    # Single digit primes don't count
    if prime in [2, 3, 5, 7]:
        continue
    # Must contain only the digits 1, 3, 5, 7, 9
    if "0" in strPrime or "2" in strPrime or "4" in strPrime or "5" in strPrime or "6" in strPrime or "8" in strPrime:
        continue
    # Cannot begin or end with a 1 or a 9
    if strPrime[0] in ["1", "9"] or strPrime[len(strPrime) - 1] in ["1", "9"]:
        continue
    # Now test if the prime is truncatable from the left
    isTruncatable = True    # So far no evidence to the contrary...
    tempStr = strPrime # Make a temp copy to truncate
    while len(tempStr) > 1:
        tempStr = tempStr[1:] # Truncate from the left
        tempNum = int(tempStr)
        if isTruncatable and tempNum in primeList:
            pass
        else:
            isTruncatable = False
    # Now test if the prime is truncatable from the right
    tempStr = strPrime
    while len(tempStr) > 1:
        tempStr = tempStr[:len(tempStr) - 1] # Truncate from the right
        tempNum = int(tempStr)
        if isTruncatable and tempNum in primeList:
            pass
        else:
            isTruncatable = False
    # HAve we found a truncatable prime?
    if isTruncatable:
        ansList.append(prime)
        if len(ansList) == 11:
            break
        
print "The list of truncatable primes so fare is:"
print ansList
print "There are %i truncatable primes" % len(ansList)
print "The sum of the truncatable primes is %i ." % sum(ansList)

while len ansList != 11:
    lenLongestTrunc = max(len(str(prime)) for prime in ansList)
    longestTrunc = [prime for prime in ansList 
                          if len(str(prime)) == lenLongestTrunc]
    print "The longest truncatable primes found so far are: ", longestTrunc
    # Longer truncatable primes are found by adding one of the digits 
        
        
        