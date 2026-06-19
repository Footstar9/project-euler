import math
k=0
n=2
while k<10_001:
    if all(n % i !=0 for i in range(2, int(math.sqrt(n))+1)):
        k+=1
    n+=1

print(n-1)