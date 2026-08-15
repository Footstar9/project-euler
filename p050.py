import math
limit = 10**6
sieve = [True] * limit
sieve[0] = sieve[1] = False
for i in range(2, math.isqrt(limit)+1):
    sieve[i*i::i] = [False] * len(sieve[i*i::i])
primes = []
for j in range(2, limit):
    if sieve[j] == True:
        primes.append(j)
answer = 0
max_steps = 0
for c in range(len(primes)):
    c_steps=1
    u = primes[c]
    steps = 1
    while u < limit:
        if c + steps >= len(primes):
            break
        if u + primes[c+steps] >=limit:
            break
        else: 
            u+=primes[c+steps]
            steps+=1
            if sieve[u]:
                c_steps = steps
    if c_steps > max_steps:
        max_steps = c_steps
        answer = u
print(answer)

    
