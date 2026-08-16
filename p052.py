n=1
while True:
    digits=[]
    for i in range(1,7):
        digits.append({c for c in str(i*n)})
    if all(x == digits[0] for x in digits):
        break
    n+=1
print(n)
