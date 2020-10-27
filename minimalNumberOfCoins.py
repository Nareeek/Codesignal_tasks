# 1
def minimalNumberOfCoins(coins, price):

    result = 0

    for i in range(len(coins) - 1, -1, -1):
        result += (price // coins[i])
        price -= (price // coins[i]) * coins[i]

    if (price):
        return -1

    return result



# 2

def minimalNumberOfCoins(coins, price):

    result = 0

    for i in range(len(coins) - 1, -1, -1):
        result += price // coins[i]
        price %= coins[i]

    if (price):
        return -1

    return result