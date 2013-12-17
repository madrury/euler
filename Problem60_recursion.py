# Problem 60

from PrimeUtilities import isPrime

def genInts(start):
    n = start
    while True:
        yield n
        n += 1
        
def genPrimes(start, stop):
    n = start
    while True:
        if n > stop:
            raise StopIteration
        if isPrime(n):
            yield n
        n += 1
        
def search(S, fdPrimes = []):
    l = len(fdPrimes)
    # Initial Step
    if l == 0:
        for p in genPrimes(2, S):
            newPrimes = fdPrimes + [str(p)]
            search(S - p, newPrimes)
    # Base case
    if l == 5 and S == 0:
        # You've got it!
        print fdPrimes
    elif l == 5:
        pass
    # Recursive step...
    if 1 <= l <= 4:
        for p in genPrimes(2, S):
            # Check if it concatenates with everything in the list...
            if (all([isPrime(int(str(p) + prStr)) for prStr in fdPrimes]) and
                all([isPrime(int(prStr + str(p))) for prStr in fdPrimes])):
                # Add to the list
                newPrimes = fdPrimes + [str(p)]
                search(S - p, newPrimes)
        
for S in genInts(26033):
    print S
    search(S)
