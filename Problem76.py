def pentagonal(n):
    return ((n*(3*n - 1)) // 2)

def generalized_pentagonal(n):
    if n % 2 == 0:
        return pentagonal((n//2) + 1)
    else:
        return pentagonal(-(n//2) - 1)

def termsign(i):
    if i % 4 < 2:
        return 1
    else:
        return -1

num_partitions = {0: 1, 1: 1}
bound = 100

def n_part(n):
    global num_partitions
    if n in num_partitions:
        return num_partitions[n]
    else:
        s, i = 0, 0
	while True:
	    k = generalized_pentagonal(i)
	    if k > n:
	        break
	    else:
	        s += termsign(i) * n_part(n - k)
		i += 1
	num_partitions[n] = s
	return s

#print n_part(100)

k = 1
while True:
    if n_part(k) % 1000000 == 0: break
    else: k += 1

print k

