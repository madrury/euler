'''
    The first two consecutive numbers to have two distinct prime factors are:
        14 = 2 * 7
        15 = 3 * 5
    The first three consecutive numbers to have three distinct prime factors are:
        644 = 2**2 *  7  * 23
        645 = 3 * 5 * 43
        646 = 2 * 17 * 19.
    Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
'''
from math import sqrt
from PrimeUtilities import factor, genPrimes, makePrimeList

print makePrimeList(100)
primeList = makePrimeList(200000)

def genInts():
    num = 2
    while True:
        yield num
        num += 1

def numDistinctPrimeFactors(n):
    factList = factor(n)
    setOfPrimeFacts = set(factList)
    return len(setOfPrimeFacts)
    
def moreThanFourFacts(n):
    numFacts = 0
    for prime in primeList:
        if prime > n:
            return False
        elif n%prime == 0:
            numFacts += 1
            n = n/prime
            if numFacts >= 4:
                return True 

numOfFacts = [None, None] # 0 and 1 dont count
for i in genInts():
    numOfFacts.append(moreThanFourFacts(i))
    if i >= 5:
        previousFour = [numOfFacts[i - 3], numOfFacts[i - 2], numOfFacts[i - 1], numOfFacts[i]]
        if all(previousFour):
            print "Found some: ",  i, i-1, i-2, i-3
        if i%1000 == 0:
            print i
        

     