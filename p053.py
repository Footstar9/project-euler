from math import comb
count = 0
for i in range(1, 101):
    for j in range(1, i+1):
        if comb(i,j)> 10**6:
            count+=1
print(count)