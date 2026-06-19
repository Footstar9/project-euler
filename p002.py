u=1
w=2
S=2
while u+w<=4*10**6:
    u=u+w
    w=u+w
    if u % 2 == 0:
        S+=u
    if w % 2 ==0:
        S+=w
print(S)