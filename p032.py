# 5 digit products are too large to satisfy pandigital criterion
import math
limit = 9999
order= [1,2,3,4,5,6,7,8,9]
pandigitals = set()
for i in range(1, math.isqrt(limit)+1):
    for j in range(i, limit // i):
        product = i * j
        digits = sorted([int(c) for c in (str(i)+str(j)+ str(product))])
        if digits == order:
            pandigitals.add(product)

print(sum(pandigitals))
