import math
number_to_divisor = [0, 1]
def sum_divisors(n):
    S= 1
    for i in range(2 , math.isqrt(n)+1):
        if n % i == 0:
            S += i
            if n // i != i:
                S += n // i
    return S
for i in range(2, 10000):
    number_to_divisor.append(sum_divisors(i))
amicable=0
print(number_to_divisor[15])
print(len(number_to_divisor))
for x in range(0, 9999):
    for y in range(0, 9999):
        if number_to_divisor[x]== y and number_to_divisor[y]==x and y !=x:
            amicable+= y
print(amicable)
