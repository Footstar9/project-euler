import math
limit = 10**6
sieve = [True] * limit
sieve[0] = sieve[1] =False
for i in range(2, math.isqrt(limit)+1):
    sieve[i*i::i]  = [False] * len(sieve[i*i::i])
composites = set()
prime_and_square = set()
for i in range(3, limit, 2):
    if sieve[i] == False:
        composites.add(i)
    else:
        k = 1
        while i + 2*(k**2) < limit:
            prime_and_square.add(i + 2*(k**2))
            k+=1
print(min(x for x in composites if x not in prime_and_square))

