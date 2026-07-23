import itertools
import math
limit = 10**5
sieve = [True] * limit
sieve[0] = sieve[1] =False
for i in range(2, math.isqrt(limit)+1):
    sieve[i*i::i]  = [False] * len(sieve[i*i::i])
u = list(itertools.permutations('1001'))
v = list("".join(u[i]) for i in range(len(u)))
print(v)

sequence = {i : True for i in range(1001, 10000)} 
for i in range(1001, 10000):
    if not sequence[i] or not sieve[i]:
        continue
    else:
        u = list(itertools.permutations(str(i)))
        v = list("".join(u[j]) for j in range(len(u)))
        for m in range(len(v)):
            for c in range(len(v)):
                for j in range(len(v)):
                    if int(v[j]) != int(v[c]) and int(v[c]) != int(v[m]):
                        if int(v[j]) - int(v[c]) == int(v[c]) - int(v[m]) and sieve[int(v[j])] and sieve[int(v[c])] and sieve[int(v[m])]:
                            print(v[j], v[c], int(v[m]))
                            break
        sequence[i] = False
