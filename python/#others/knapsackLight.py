# 1
def knapsackLight(value1, weight1, value2, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return value1 + value2
    if min(weight1, weight2) > maxW:
        return 0
    if weight1 <= maxW and (value1 >= value2 or weight2 >= maxW):
        return value1
    return value2


# 2
def knapsackLight2(weight1, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return 'both'
    if min(weight1, weight2) > maxW:
        return 'none'
    if max(weight1, weight2) <= maxW:
        return 'either'
    if weight1 <= maxW:
        return 'first'
    return 'second'
