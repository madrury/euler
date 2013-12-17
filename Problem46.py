'''
    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
        9 = 7 + 212
        15 = 7 + 222
        21 = 3 + 232
        25 = 7 + 232
        27 = 19 + 222
        33 = 31 + 212
    It turns out that the conjecture was false.
    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
from __future__ import division
from math import sqrt
from PrimeUtilities import genPrimes, isPrime

def genOdd(init = 9):
    n = init
    while True:
        yield n
        n += 2
    
def genOddComposities():
    primeStream = genPrimes()
    prime = primeStream.next() # 2
    prime = primeStream.next() # 3
    for i in genOdd(init = 3):
        if i < prime:
            yield i
        elif i == prime:
            prime = primeStream.next()
        
    
def isTwiceSquare(n):
    '''Tests if an integer is twice a square.'''
    if n%2 == 1:
        return False
    else:
       m = n/2
       testNum = sqrt(m)
       return int(testNum) == testNum  # Is integer?
    
# Solve the problem
for odd in genOddComposities():
    isFound = False
    if isFound:
        break
    primeStream = genPrimes()
    prime = primeStream.next() # 2
    while prime < odd:
        remainder = odd - prime
        if isTwiceSquare(remainder):
            print odd, " = ", prime, " + ", remainder
            break
        prime = primeStream.next()
        if prime > odd:
            print "FOUND :", odd
            isFound = True

        


