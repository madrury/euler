#!/usr/local/bin/python

'''
Project Euler Problem # 35
    "The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
     There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
     How many circular primes are there below one million?"
'''

# We need a list of all the primes less than 1 million
from PrimeUtilities import makePrimeList
primeLookup = makePrimeList(1000000)

from StringUtilities import rotations
# Solve the problem
ansList = []
for prime in primeLookup:
    # We may have already found it!
    if prime in ansList:
        continue
    # If it contains an even digit or a five it cannot be a circular prime
    if "0" in str(prime) or "2" in str(prime) or "4" in str(prime) or "5" in str(prime) or "6" in str(prime) or "8" in str(prime):
        continue
    # Otherwise let's check the rearrangements
    testList = [int(numStr) for numStr in rotations(str(prime))]
    test = True   # Test flag for if all ints in testList are primes
    for testInt in testList:
        if test == True and testInt in primeLookup:
            pass   # Test passed
        else:
            test = False   # Test failed
    # After rolling off, if test is still true, all rearrangements are prime
    if test == True:   
        ansList.extend(testList)  # Everything in the list is a circular prime

print ansList
print "There are %i circular primes less than 1000000." % len(ansList)




    