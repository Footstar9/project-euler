import math
def is_prime(n):
    if all(n % i !=0 for i in range(2, int(math.sqrt(n))+1)):
        return True
    else:
        return False
S=0
for i in range (2, 2*(10**6)):
    if is_prime(i):
        S+=i
print(S)