
def chain(u):
    n=1
    while u>1:
        n+=1
        if u % 2 ==0:
            u//=2
        else:
            u=3*u+1
    return n
M=0
number=0
for i in range(1, 10**6):
    m=chain(i)
    if m>M:
        M=m
        number=i
print(number)
