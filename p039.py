import math
solutions= {}
for p in range(1001):
    for c in range(math.floor(p / 3), math.ceil(p/2)+1):
        for b in range(math.floor((p-c)/2), c):
            a = p - (b+c)
            if a**2 + b**2 == c**2:
                solutions[p] = solutions.get(p, 0) + 1

print(max(solutions, key=solutions.get))
