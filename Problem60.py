# Problem 60

from PrimeUtilities import isPrime

def genInts(start):
    n = start
    while True:
        yield n
        n += 1
        
def genPrimes(start, stop = None):
    n = start
    if stop == None:
        while True:
            if isPrime(n):
                yield n
            n += 1
    else:
        while True:
            if n > stop:
                raise StopIteration
            if isPrime(n):
                yield n
            n += 1

def concatPrime(p, q):
    return (isPrime(int(str(p) + str(q))) and isPrime(int(str(q) + str(p))))
    
assert concatPrime(3, 7)
        
for p1 in genPrimes(11):
    print p1
    for p2 in genPrimes(7, p1):
        if concatPrime(p1, p2):
            for p3 in genPrimes(5, p2):
                if concatPrime(p3, p1) and concatPrime(p3, p2):
                    for p4 in genPrimes(3, p3):
                        if (concatPrime(p4, p1) and concatPrime(p4, p2) and
                            concatPrime(p4, p3)):
                            for p5 in genPrimes(2, p4):
                                if (concatPrime(p5, p1) and concatPrime(p5, p2) and
                                    concatPrime(p5, p3) and concatPrime(p5, p4)):
                                        print p1, p2, p3, p4, p5
                                        print sum(p1, p2, p3, p4, p5)