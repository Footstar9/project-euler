import math
import random
print(math.comb(40,20))

lengrid = 5
def sumdigits(str):
    digits= [int(c) for c in str]
    return sum(i for i in digits)

strings=[""]

end= False
while end == False:
    new_strings=[]
    for s in strings:
        if sumdigits(s) + (2*lengrid - len(s)) > lengrid and sumdigits(s) < lengrid:
            new_strings.append(s + "0")
            new_strings.append(s + "1")
        elif sumdigits(s) < lengrid and len(s) < 2*lengrid:
            new_strings.append(s + "1")
        elif len(s) < 2*lengrid:
            new_strings.append(s + "0")
        else:
            new_strings.append(s)
    if strings == new_strings:
        end= True
        break
    strings= new_strings

print(len(new_strings))
print(math.comb(2*lengrid, lengrid))

n = 2
grid = [[1] * (n + 1) for _ in range(n + 1)]   # edges are all 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]
        print(grid)
print(grid[n][n])