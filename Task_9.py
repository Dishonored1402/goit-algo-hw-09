### Функція жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}

    for coin in coins:
        if amount >= coin:
            coin_count[coin] = amount // coin
            amount %= coin
        if amount == 0:
            break

    return coin_count



amount = 113
coins_used = find_coins_greedy(amount)
print(coins_used)



### Функція динамічного програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    coin_count = {}
    remaining_amount = amount
    while remaining_amount > 0:
        for coin in coins:
            if remaining_amount >= coin and dp[remaining_amount] == dp[remaining_amount - coin] + 1:
                if coin in coin_count:
                    coin_count[coin] += 1
                else:
                    coin_count[coin] = 1
                remaining_amount -= coin
                break

    return coin_count



amount = 113
coins_used = find_min_coins(amount)
print(coins_used)