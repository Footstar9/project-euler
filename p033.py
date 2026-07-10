def simplify(i,j):
    if i == 1:
        return (i,j)
    for d in range(2, i+1):
        if i % d == 0 and j % d ==0:
            return simplify(i // d, j // d)
    return (i,j)
final = []
for i in range(10, 100):
    digits_1 = [int(c) for c in str(i)]
    for j in range(i+1, 100):
        digits_2 = [int(c) for c in str(j)]
        if 0 not in digits_1 or 0 not in digits_2:
            for c in digits_1:
                if c in digits_2:
                    new_digits_1 = [x for x in digits_1 if x!=c]
                    new_digits_2 = [x for x in digits_2 if x!=c]
                    if len(new_digits_1)>0 and len(new_digits_2)>0 and new_digits_2[0] != 0:
                        # print(f" pair is {i,j}, correct simplification is {simplify(i,j)}, inexperienced simplificatioj is {simplify(digits_1[0],digits_2[0])}")
                        if simplify(i,j) == simplify(new_digits_1[0],new_digits_2[0]):
                            final.append((i,j))
numerator=1
denominator = 1
for c in final:
    numerator *= c[0]
    denominator*=c[1]

print(simplify(numerator, denominator))

