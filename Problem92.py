#  A number chain is created by continuously adding the square of the digits in a
#  number to form a new number until it has been seen before.
# 
#  Any chain that arrives at 1 or 89 will become stuck in an endless
#  loop. What is most amazing is that EVERY starting number will eventually arrive
#  at 1 or 89.
# 
#  How many starting numbers below ten million will arrive at 89?

# Only compute once
squares = {x: x**2 for x in range(10)}
endpts = set([1, 89])

# Memoize for fun and profit
memo = {}
def ends_at_89(n):
    if n%10000 == 0: print n
    orign = n
    while n not in endpts:
        n = sum(squares[int(d)] for d in str(n))
	if n in memo: return memo[n]
    if orign < 10**4: memo[orign] = (n == 89)
    return n == 89

print "--- Testing ---"
print "44 Ends at 1, should print false: ", ends_at_89(44)
print "85 Ends at 89, should print true: ", ends_at_89(85)

print "--- Solution ---"
print sum(ends_at_89(n) for n in xrange(1, 10*10**6))
