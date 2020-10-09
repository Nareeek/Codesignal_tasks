def piecesOfDistinctLengths(strawLength):
    sum = 0
    for i in range(1, strawLength + 1):
        sum += i
        if sum > strawLength:
            return i - 1
        
        