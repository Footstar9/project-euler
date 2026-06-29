maximum_digits = 1
while len(str(maximum_digits * (9**5))) > maximum_digits:
    maximum_digits+=1
maximum_number = 10**(maximum_digits) - 1
correct_numbers = set()
for i in range(2, maximum_number+1):
    sum_digits = sum(int(c)**5 for c in str(i))
    if sum_digits == i:
        correct_numbers.add(i)
print(sum(correct_numbers))