import math
def is_square(n):
    return math.isqrt(n)**2 == n
def is_pentagonal(n):
    u = 1 + 24*n
    return is_square(u) and (1+ math.isqrt(u))%6 ==0
def is_hexagonal(n):
    u = 1+8*n
    return is_square(u) and (1+math.isqrt(u))%4 == 0
triangulars = [n*(n+1) // 2 for n in range(10**6)]
special_number = 0
step = 1
while special_number == 0:
    candidate = triangulars[285+step]
    if is_pentagonal(candidate) and is_hexagonal(candidate):
        special_number = candidate
    step+=1
print(candidate)