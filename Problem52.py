'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def digHist(n):
	H = dict((str(n),0) for n in range(10))
	S = str(n)
	for dig in S:
		H[dig] += 1
	return H
	
def genInts(init):
	n = init
	while True:
		yield n
		n += 1
	
print digHist(123566)

# Loop over the number of digits	
for n in genInts(1):
	for i in range(10**n, 10**(n+1)/6 + 1):
		H1 = digHist(i)
		H2 = digHist(2*i)
		H3 = digHist(3*i)
		H4 = digHist(4*i)
		H5 = digHist(5*i) 
		H6 = digHist(6*i)
		if H1 == H2 == H3 == H4 == H5 == H6:
			print i, 2*i, 3*i, 4*i, 5*i, 6*i
			