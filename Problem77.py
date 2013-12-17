from primes import sieve
N = 10000
primes = list(sieve(N))

prime_partitions = {n: 0 for n in range(N + 1)}
prime_partitions[0] = 1

for p in primes:
    for n in range(p, N+1):
        prime_partitions[n] += prime_partitions[n - p]

print [n for n in prime_partitions if prime_partitions[n] > 5000][0]
