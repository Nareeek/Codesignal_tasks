def nearestRoundNumber(value):

    while value % 10 != 0:
        value += 1
    return value