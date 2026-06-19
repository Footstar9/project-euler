
N=600851475143
p=1
def smallest_divisor(n):
    if n==1:
        d=1
    else:
        d=2
        while n % d !=0:
            d=d+1
    return d

while N>=2:
    s=smallest_divisor(N)
    N=N//s
    if s>p:
        p=s
print(p)

