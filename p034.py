from math import factorial
n=1
while n*factorial(9) >= 10**(n - 1):
    n+=1
# We found 8*9!<10^7 
# (the maximum factorial digit sum of an 8 digit number is smaller than the smallest 8 digit number)
# then we only have to scan up to 7 digit numbers, so our limit is 10^7-1
limit = 10**(n-1) -1
total = 0
for i in range(3, limit +1):
    S=0
    digits= str(i)
    for digit in digits:
        S+=factorial(int(digit))
    if S == i:
        total+=i
print(total)
