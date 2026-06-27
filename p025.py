n=2
a=1
b=1
while len(str(b)) < 1000:
        n+=1
        a,b= b, a+b

print(n)