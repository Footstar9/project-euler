# since n>1 the maximum possible integer would be a 4 digit integer
def construct_pandigital(n, k, step):
    pandigital = str(n)
    pandigital_set = {int(c) for c in pandigital}
    if len(pandigital)<9:
        digits = str(k*step)
        digits_set = {int(c) for c in digits}
        if len(pandigital) == len(pandigital_set) and 0 not in pandigital_set and len(digits) == len(digits_set) and 0 not in digits_set:
            if all(digits[j] != pandigital[i] for i in range(len(pandigital)) for j in range(len(digits))):
                return construct_pandigital(int(pandigital + digits), k, step+1)
    if len(pandigital) == 9:
        return pandigital
    else:
        return 0

limit = 10**4
M=0
for i in range(limit):
    m = int(construct_pandigital(i,i,2))
    if m>M:
        M=m
print(M)