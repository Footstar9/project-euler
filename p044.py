# We found D > P(k-j) for k>j, effectively we are trying to minimise k-j
import math
def sum_is_pentagonal(k,j):
    c = 1 -12*(j + k - 3*(j**2 +k**2))
    u = math.isqrt(c)
    if u**2 == c and (1 + u) % 6 == 0:
        return True
    else:
        return False

def difference_is_pentagonal(k,j):
    p = 1 - 12 * (k - j - 3*(k**2 - j**2))
    u= math.isqrt(p)
    if u**2 == p and (1+u) % 6 == 0:
        return True
    else:
        return False
limit = 10**4
D = limit * (3*limit-1) // 2
for k in range(2, limit):
    Pk = k * (3*k-1) // 2
    for j in range(k-1,0, -1):
        Pj = j * (3*j-1) // 2
        if Pj < 3*k+1:
            break
        if sum_is_pentagonal(k,j) and difference_is_pentagonal(k,j):
            d = Pk-Pj
            if d < D:
                D = d
            break
print(D)

