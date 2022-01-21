n = 1260
coins = [500, 100, 50, 10]
result = 0
for coin in coins:
    count = n // coin
    n %= coin
    result += count

print(result)