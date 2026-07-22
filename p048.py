s = sum(i**i for i in range(1,1001))
digits = [int(c) for c in str(s)]
print("".join(str(digits[i]) for i in range(len(digits)-10, len(digits), 1)))
