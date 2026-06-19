s=0
N=100
for i in range(1, 101):
    s+=i**2
S=(N*(N+1)//2)**2
d=S-s
print(d)