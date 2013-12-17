'''
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''

def digSum(n):
	S = str(n)
	return sum(int(dig) for dig in S)
	
M = 1
for i in range(1, 101):
	for j in range(1, 101):
		x = digSum(i**j)
		if x > M:
			M = x
			
print M