l=0
for i in range (100,1000):
    for k in range (100, 1000):
        n=i*k
        s=str(n)
        if s==s[::-1] and n>l:
            l=n

print(l)