
d=1
M=0
d_max = 0
while d < 1000:
    remainders= []
    next_remainder = 10% d
    while next_remainder not in remainders:
        remainders.append(next_remainder)
        next_remainder = (remainders[-1]* 10) % d
    for i in range(len(remainders)):
      if remainders[i] == next_remainder:
            m= len(remainders) - i
    if m > M:
        M= m
        d_max = d
    d+=1
print(d_max)



    