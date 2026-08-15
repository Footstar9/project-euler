from itertools import combinations
import math
limit = 10**6
sieve = [True] * limit
sieve[0] = sieve[1] = False
for i in range(2,math.isqrt(limit) +1):
    sieve[i*i::i] = [False] * len(sieve[i*i::i])

def property(n):
    digits = [c for c in str(n)]
    max_primes_for_number = 0
    smallest_prime = 0
    for i in range(1, len(digits)):

        for comb in combinations(range(len(digits)),i):
            new_digits = [c for c in str(n)]
            small_number = float('inf')
            primes_for_comb = 0
            for k in range(10):
                if k== 2 and primes_for_comb == 0:
                    break
                if 0 in comb and k == 0:
                    continue
                for c in comb:
                    new_digits[c] = str(k)
                u = int("".join(new_digits))
                if sieve[u]:
                    primes_for_comb+=1
                    if u < small_number:
                        small_number = u
            if primes_for_comb > max_primes_for_number:
                max_primes_for_number = primes_for_comb
                smallest_prime = small_number
    return (smallest_prime, max_primes_for_number)
            

k=11
while property(k)[1] < 8:
    k+=2
print(property(k)[0])