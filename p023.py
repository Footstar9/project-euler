limit = 28123 + 1
sum_divisors = [0] * limit
for d in range(1, limit // 2 + 1):
    n=2
    while n * d < limit:
        sum_divisors[n * d] += d
        n+=1
is_abundant = []
for i in range(len(sum_divisors)):
    if i < sum_divisors[i]:
        is_abundant.append(i)
two_abundant = [False] * limit
for x in is_abundant:
     for y in is_abundant:
          if x+y< limit:
               two_abundant[x+y] = True

print(sum(i for i in range(limit) if two_abundant[i]== False))


total=0
s= set(is_abundant)
def sum_two_abundant(n):
    for x in s:
        y= n-x
        if y in s:
            return True
    return False
for c in range(1, limit):
        if not sum_two_abundant(c):
             total+=c
print(total)
