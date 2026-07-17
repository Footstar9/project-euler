from math import factorial
pandigitals = {1, 2, 3, 4, 5 ,6, 7, 8, 9}
primes = [2,3,5,7,11,13,17]
while len(str(next(iter(pandigitals)))) < 10:
    new_pandigitals = set()
    for c in pandigitals:
        for i in range(10):
            if str(i) not in str(c):
                new_pandigitals.add(int(str(c) + str(i)))
    pandigitals = new_pandigitals


def special_number(n):
    string = str(n)
    return all(int(string[i:i+3]) % primes[i-1] == 0 for i in range(1,8))

print(pandigitals)
print(special_number(1406357289))
print(1406357289 in pandigitals)
print(sum(x for x in pandigitals if special_number(x)))
S=0
for x in pandigitals:
    if special_number(x):
        S+=x
print(S)

