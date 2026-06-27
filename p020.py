facto = 1
for i in range(1, 101):
    facto *= i
digits = [int(c) for c in str(facto)]
print(sum(digits))