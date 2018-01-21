def sieve(N):
    '''True implementation of the prime sieve.
         
	 Iterator that returns the primes of up to and including N
       in order.
    '''
    could_be_prime = [True]*(N+1)
    # 0 and 1 are not prime
    could_be_prime[0] = could_be_prime[1] = False
    for i in xrange(N):
        # If we have not explicitly marked as composite yet...
	if could_be_prime[i]:
	    yield i
	    # Mark all multiples of this prime as composite
	    for j in xrange(i*i, N, i):
	        could_be_prime[j] = False

def euler_totients(N):
    '''A sieve type algorithm for calculating the Euler totients of
    the first N integers.
       
      This uses the prime factorization formula for the totient and
    the standard prime sieve to build up the totients of the numbers
    in the entire list [0 ... N].
    '''
    # Initialize all totients to one, as we do not know of any prime
    # factors yet.
    totients = [1]*(N+1)
    # Skip zero and one...
    for i in xrange(2, N+1):
        # If the totient of i is 1 at this point, it is a prime.
        if totients[i] == 1:
        # Update the totients of the multiples of i by multiplying 
	    # the current value by i^(n-1)*(i - 1), where n is the 
	    # largest power of i dividing the multiple.
	    for j in xrange(i, N+1, i):
		    totients[j] *= (i - 1)
		# Guarenteed to divide out, k is an integer.
		k = j / i
		# Divide out the prime powers...
		while(k % i == 0):
		    totients[j] *= i
		    k /= i
    return totients
		    
