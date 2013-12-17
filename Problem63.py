
def lenNum(n):
	return len(str(n))

count = 0
for e in range(22):
	for i in range(10):
		test = i**e
		if lenNum(test) == e:
			print test
			count += 1
			
print count