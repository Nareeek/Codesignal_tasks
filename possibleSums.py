def possibleSums(coins, quantity):
    possible_sums = {0}
    for coin, quant in zip(coins, quantity):
        for s in set(possible_sums):
            for quant in range(1, quant + 1):
                possible_sums.add(coin * quant + s)
    return len(possible_sums) - 1


print(possibleSums([10, 50, 100], [1, 2, 1]))
