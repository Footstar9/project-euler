import math
def is_square(n, j, i):
    for c in range(max(i,j), math.isqrt(n)+1):
        if n == c**2:
            return True
        else: continue
    return False
triplet= False
while triplet == False:
    for i in range(1, 500):
        for j in range (i, 500):
            s=i**2+j**2
            if is_square(s, j, i) and i+j+math.isqrt(s)==1000:
                triplet = True
                print(f"answer is {i*j*math.isqrt(s)}")



