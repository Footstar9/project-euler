from math import prod
def digit(n):
    v=1
    while v*(10**v) - sum(10**i for i in range(0, v)) < n:
        v+=1
    k= v-1
    q= (n- (k*(10**k) - sum(10**i for i in range(0, k)))) // (k+1)
    if (n- (k*(10**k) - sum(10**i for i in range(0, k)))) % (k+1) == 0:
        u= 10**(k) + q -1
        digits = [int(c) for c in str(u)]
        return digits[-1]
    else:
        u = 10**(k) + q
        digits = [int(c) for c in str(u)]
        return digits[((n- (k*(10**k) - sum(10**i for i in range(0, k))))%(k+1))-1]

print(prod(digit(10**i) for i in range(7)))

