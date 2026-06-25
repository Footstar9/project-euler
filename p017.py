digit_to_letter = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
ten_to_letter = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
additional = {"hundred": 7, "and" : 3, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, "one thousand": 11}

def number_to_letter(n):
    s=str(n)
    digits= [int(c) for c in s]
    sum_letter=0
    if len(digits)== 3:
        sum_letter+=digit_to_letter[digits[0]] + additional["hundred"]
        if digits[1]>1:
            sum_letter+= additional["and"]+ ten_to_letter[digits[1]] + digit_to_letter[digits[2]]
        if digits[1]==1:
            sum_letter+= additional["and"] + additional[int("1"+str(digits[2]))]
        if digits[1]==0 and digits[2]!=0:
            sum_letter+= additional["and"] + digit_to_letter[digits[2]]

    if len(digits)==2:
        if digits[0]>1:
            sum_letter+=ten_to_letter[digits[0]] + digit_to_letter[digits[1]]
        if digits[0]==1:
            sum_letter+= additional[int("1"+str(digits[1]))]
    if len(digits)==1:
        sum_letter+=digit_to_letter[digits[0]]
    return sum_letter

print(sum(number_to_letter(i) for i in range(1,1000))+ additional["one thousand"])