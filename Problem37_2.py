'''
    "The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at          
     each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

     Find the sum of the only eleven primes that are both truncatable from left to right and right to left."
'''

from PrimeUtilities import makePrimeList, isPrime
primeList = makePrimeList(1000000)

isPrime(200)

# Now solve the problem
ansList = []
ansListLeft = [2, 3, 5, 7]
ansListRight = [2, 3, 5, 7]
for prime in primeList:
    strPrime = str(prime)  # String representation of the prime under constideration
    # Single digit primes don't count
    if prime in [2, 3, 5, 7]:
        continue
    # Must contain only the digits 1, 3, 5, 7, 9 to be a substring of a truncatable prime
    if ("0" not in strPrime and "4" not in strPrime and 
        "6" not in strPrime and "8" not in strPrime):  
        # Left truncatable primes cannot end with a 1 or a 9         # Now test if the prime is truncatable from the left
        tempStr = strPrime[1:] # The left truncated number
        tempNum = int(tempStr) 
        if tempNum in ansListLeft:  # If left truncatable, the truncate is a shorter left truncatable prime
           ansListLeft.append(prime)
        # Right truncatable primes cannot begin with a 1 or a 9
        # Now test if the prime is truncatable from the right
        tempStr = strPrime[:len(strPrime) - 1] # Right truncate
        tempNum = int(tempStr)
        if tempNum in ansListRight: # If right truncatable, the right truncate is a shorter right truncatable prime
            ansListRight.append(prime)
        if prime in ansListLeft and prime in ansListRight:
            ansList.append(prime)

# What do we have now?
print ansListLeft
print ansListRight
print ansList

while len(ansList) < 11:
    # Find more left truncatable primes
    # First find the longest left truncatable primes so far found
    maxLen = max(len(str(n)) for n in ansListLeft)
    print "MAX LEN: ", maxLen
    longLeftList = [n for n in ansListLeft if len(str(n)) == maxLen] 
    # Exapand the left truncatable primes
    for dig, leftPrime in [(D, N) for D in [1, 3, 5, 7, 9]
                                  for N in longLeftList]:
        newNum = int(str(dig) + str(leftPrime)) # Make a new canidate by appending a digit on the left
        if isPrime(newNum):
            ansListLeft.append(newNum)
            print "LEFT: ", ansListLeft
    # Find more right truncatable primes
    # First find the longest right truncatable primes so far found
    maxLen = max(len(str(n)) for n in ansListRight)
    longRightList = [n for n in ansListRight if len(str(n)) == maxLen]    
    # Exapand the left truncatable primes
    for dig, rightPrime in [(D, N) for D in [1, 3, 5, 7, 9]
                                   for N in longRightList]:
        newNum = int(str(rightPrime) + str(dig)) # Make a new canidate by appending a digit on the left
        if isPrime(newNum):
            ansListRight.append(newNum)
            print "RIGHT: :", ansListRight
    ansList = list((set(ansListLeft) & set(ansListRight)) - set([2, 3, 5, 7]))
    print ansList

print sum(ansList)
        
        
        
        
