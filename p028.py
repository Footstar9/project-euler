n = 1001
S=1
for i in range(3, n+1, 2):
    S+= i**2 + (i**2 - (i - 1)) + (i**2 - 2*(i-1))+ (i**2 - 3*(i-1))
print(S)