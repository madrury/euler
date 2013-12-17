'''
    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
        9 = 7 + 2*1**2
        15 = 7 + 2*2**2
        21 = 3 + 2*3**2
        25 = 7 + 2*3**2
        27 = 19 + 2*2**2
        33 = 31 + 2*1**2
    It turns out that the conjecture was false.
    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
from __future__ import division
from math import sqrt
from PrimeUtilities import genPrimeList, genTwiceSquareList, genOddComposites, genPrimes

def isTwiceSquare(n):
    '''Tests if an integer is twice a square.'''
    if n%2 == 1:
        return False
    else:
       m = n/2
       testNum = sqrt(m)
       return int(testNum) == testNum  # Is integer?
    
def genEllShapes():
    '''Generate the L shaped blocks of numbers used in this problem.'''
    # Initialize both the stream of primes and the stream of squares
    primeListStream = genPrimeList() # [2], [2, 3], [2, 3, 5], ...
    primeList = primeListStream.next() # [2]
    squareListStream = genTwiceSquareList() # [2], [2, 8], [2, 8, 18], ...
    squareList = squareListStream.next() # [2]
    while True:
        # Initialize the list to return
        L = []
        maxPrime = max(primeList)
        maxSquare = max(squareList)
        # Yielding L shapes of the form:
        #     maxPrime * squareList + primeList * maxSquare
        for square in squareList:
            L.append((maxPrime, square))
        for prime in primeList:
            L.append((prime, maxSquare))
        L.pop() # We have the (max, max) twice, kill the last one
        yield L
        primeList = primeListStream.next()
        squareList = squareListStream.next()

# Now solve the problem
# Generating the stream of ell shapes
ellStream = genEllShapes()
ellShape = ellStream.next() # [(2,2)]
# Keep track of what prime we're on
primeStream = genPrimes()
p = primeStream.next() # 2
# Generate odd composites
oddCompStream = genOddComposites()
oddComp = oddCompStream.next() # 9
# Numbers found
numFound = set([])
finished = False
while True:
    # Generate the new summands from the ell shape we are on
    for (prime, square) in ellShape:
        numFound.add(prime + square)
    # Check if we've found all the odd composites less than the prime we are on
    while oddComp < prime:
        # Here are the ones we've found
        if oddComp in numFound:
            oddComp = oddCompStream.next()
        # We havent found this one!
        else:
            ans = oddComp
            print "Found one!", ans
            oddComp = oddCompStream.next()
        # Have we finished?
    if finished:
        break
    # If not, advance all the iterators and keep going
    else:
        ellShape = ellStream.next()
        p = primeStream.next()
 

        
            






        
    
     


        


