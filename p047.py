import math
limit = 10**6
sieve = [True] * limit
sieve[0] = sieve[1] =False
for i in range(2, math.isqrt(limit)+1):
    sieve[i*i::i]  = [False] * len(sieve[i*i::i])
def distinct_primes(n, primes =None):
    if primes is None:
        primes = set()
    if n > 1 and not sieve[n]:
        for i in range(2, math.isqrt(n)+1):
            if not sieve[i]:
                continue
            elif n % i == 0:
                primes.add(i)
                return distinct_primes(n // i, primes)
    if sieve[n]:
        primes.add(n)
        return len(primes)
for i in range(644, 647):
    print(distinct_primes(i))
n= 1
while True:
    if distinct_primes(n) == 4:
        if all(distinct_primes(n+i) == 4 for i in range(1,4)):
            break
    n+=1
print(n)