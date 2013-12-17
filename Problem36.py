'''Project Euler Problem # 36
   "The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    (Please note that the palindromic number, in either base, may not include leading zeros.)
'''
from math import log

# First we need a utility for converting to binary
def toBianary(num):
	'''One line bitches!'''
	return ''.join([str(int(bool(num&(2**i)))) for i in range(int(log(num, 2)),-1,-1)])

def isPalindrome(iterable):
	'''Check if an iterator is a palendrome'''
	for i in range(len(iterable)/2 + 1):
		if iterable[i] != iterable[len(iterable) - i - 1]:
			return False
	return True
	
# Now solve the problem
resList = []
for num in range(1, 1000000):
    num_10 = str(num)
    num_2 = toBianary(num)
    if isPalindrome(num_10) and isPalindrome(num_2):
        resList.append(num)

print resList
print "The number of dual-palindromic numbers is %i" % sum(resList)