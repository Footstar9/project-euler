import math
from math import factorial
#limit = 987654321
#sieve = [True] * (limit+1)
#sieve[0] = sieve[1] = False
#for d in range(2, math.isqrt(limit)+1):
    #sieve[d*d::d] = [False] * len(sieve[d*d::d])
# best =0
#for i in range(limit+1):
    #digits = int(len([c for c in str(i)]))
    #if sieve[i] == False:
        #continue
    #else:
        #if set(str(i)) == set(str(j) for j in range(1,digits+1)):
            #best = max(best, i)

#print(best)
def is_prime(a):
    return all(a % d != 0 for d in range(2, math.isqrt(a)+1))

def perm_digit(n):
    permutations =[str(i) for i in range(1,n+1)]
    while len(permutations[0]) < n:
        new_permutations = []
        for c in permutations:
            for i in range(1,n+1):
                if str(i) not in str(c):
                    new_permutations.append(str(c) + str(i))
        permutations = new_permutations
    return set(permutations)
best = 0
for i in range(2,10):
    for c in perm_digit(i):
        if is_prime(int(c)) == False:
            continue
        else:
            best = max(best, int(c))
print(best)
    
