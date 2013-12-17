from PrimeUtilities import makePrimeList

def main():
    primes = makePrimeList(1000000)
    largest = 0
    chain = []
    for start in range(10):
        seq = primes[start:]
        i = 0
        total = 0
        for prime in seq:
            total += prime
            if total > 1000000:
                break
            i += 1
            if total in primes:
                c = seq[:i]
                if len(c) > len(chain):
                    chain = c
    print sum(chain)

if __name__ == "__main__":
    main()