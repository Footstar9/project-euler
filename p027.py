import math
def is_prime(n):
    if n <= 1:
        return False
    
    sieve = [True] * (n+1)
    sieve[0]=sieve[1]=False
    for d in range(2, math.isqrt(n)+1):
        q=2
        while d*q <= n:
            sieve[d*q] = False
            q+=1
    if sieve[n] == True:
        return True
    else:
        return False


# suppose no primes greater than a million

limit = 10**6
sieve = [True] * (limit+1)
sieve[0]=sieve[1]=False
for d in range(2, math.isqrt(limit)+1):
        q=2
        while d*q <= limit:
            sieve[d*q] = False
            q+=1

primes = {i for i in range(len(sieve))if sieve[i] == True}

def consecutive_primes(a,b):
    n=0
    u = b
    while u in primes:
        n+=1
        u = n**2 + a*n + b
    return n

M=0
ab = 0
for a in range(-999, 1000):
    for b in primes:
        if b <= 1000:
            m=consecutive_primes(a,b)
            if m > M:
                M= m
                ab= a*b
        else:
            continue

print(ab)
        
        
    


