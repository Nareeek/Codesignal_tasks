def depositProfit(deposit, rate, threshold):
    s = 100
    q = 0
    increase = (1 + rate / 100)
    while True:
        if s < threshold:
            s *= increase
            q += 1
        elif s >= threshold:
            return q


print(depositProfit(100, 1, 101))
