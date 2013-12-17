'''
Project Euler Problem # 57:

t is possible to show that the square root of two can be expressed as an infinite continued fraction.

 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''

def numDigits(n):
	return len(str(n))

# Initialize the numerator and denominator list to the first convergents
numerators = [1, 3]
denominators = [1, 2]

# Use the recursion relation to find the numerators and denominators of subsequent convergents
# Note that these are automatically relatively prime by the determinant relation
# Note also that the continued fraction expansion of root(2) is [1; 2, 2, 2, 2, 2, ...]
for i in range(2, 1001):
	numerators.append(2*numerators[i-1] + numerators[i-2])
	denominators.append(2*denominators[i-1] + denominators[i-2])
	
print sum(1 for i in range(1001) if numDigits(numerators[i]) > numDigits(denominators[i]))

