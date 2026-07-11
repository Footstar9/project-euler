import math
limit = 10**6
sieve = [True] * limit
sieve[0] = sieve[1]= False
for d in range(2, math.isqrt(limit) +1):
    sieve[d*d::d] = [False] * len(sieve[d*d::d])
def is_truncatable(n):
    digits = str(n)
    if all(sieve[int(digits[i:])] == True for i in range(len(digits)))and all(sieve[int(digits[:i])] == True for i in range(1, len(digits)+1)):
        return True
    else:
        return False
n=0
j=10
S=0
while n < 11:
    if sieve[j] == True and is_truncatable(j):
        n+=1
        print(j)
        S+=j
    j+=1
print(S)