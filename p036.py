def binary(n):
    if n==1:
        return("1")
    if n % 2 ==0:
        return(binary(n // 2) + "0")
    else:
        return(binary(n//2) + "1")
S=0
for i in range(1, 10**6):
    num = str(i)
    if num == num[::-1]:
        bin = binary(i)
        if bin == bin[::-1]:
            S+=i
print(S)