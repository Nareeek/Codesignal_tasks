def stringsCrossover(inputArray, result):
    aLen = len(inputArray)
    sLen = len(result)
    pairs = 0
    for i in range(0,aLen):
        for j in range(i+1,aLen):
            crossover = True
            for k in range(0,sLen):
                if inputArray[i][k]!=result[k] and inputArray[j][k]!=result[k]:
                    crossover = False
                    break
            if crossover:
                pairs += 1
    return pairs