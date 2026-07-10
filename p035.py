import math
limit = 10**6
sieve = [True] * limit
sieve[0] = sieve[1]= False
for d in range(2, math.isqrt(limit) +1):
    sieve[d*d::d] = [False] * len(sieve[d*d::d])
def rotate_digits(n):
    perms=[]
    digits = str(n)
    perms.append(int(digits))
    for _ in range(len(digits)-1):
        new_digits = str()
        for i in range(0, len(digits)):
            new_digits+= digits[i-1]
        perms.append(int(new_digits))
        digits = new_digits
    return perms
cache = {}
circular = set()
for i in range(limit):
    if cache.get(i) == False:
        continue
    if cache.get(i) == True:
        continue
    if sieve[i] == False:
        cache[i] = False
        continue
    rot = rotate_digits(i)
    if all(sieve[nums] == True for nums in rot):
        for n in rot:
            cache[n] = True
            circular.add(n)
            
    else:
        for n in rot:
            cache[n] = False
print(len(circular))





    
