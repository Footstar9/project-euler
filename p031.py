coins = {1 : 1, 2: 2, 3:5, 4:10, 5:20, 6:50, 7:100, 8:200}
def ways(amount, k):
    if k == 1 or amount == 0:
        return 1
    elif amount - coins[k] < 0:
        return ways(amount, k-1)
    elif amount - coins[k]>=0:
        return ways(amount, k-1) + ways(amount - coins[k], k)

print(ways(200, 8))