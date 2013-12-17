'''
     We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit  
     pandigital and is also prime.

     What is the largest n-digit pandigital prime that exists?
'''

from PrimeUtilities import isPrime
from StringUtilities import rearrangements

ansList = []
for numStr in rearrangements('1234567'):
	num = int(numStr)
	if isPrime(num):
		ansList.append(num)
		
print ansList
print max(ansList)