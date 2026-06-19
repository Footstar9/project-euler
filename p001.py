print(sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0))
print(sum(i for i in range(0,1000,3)) + sum(i for i in range(0,1000,5)) - sum(i for i in range(0,1000,15)))