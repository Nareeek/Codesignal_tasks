def electionsWinners(votes, k):

    currentMaxIndex = 0
    cntLeaders = 0
    result = 0
    for i in range(0, len(votes)):
        if votes[i] == votes[currentMaxIndex]:
            cntLeaders += 1
        if votes[i] > votes[currentMaxIndex]:
            currentMaxIndex = i
            cntLeaders = 1

    for i in range(len(votes)):
        if votes[i] + k > votes[currentMaxIndex]:
            result += 1
        if (votes[i] + k == votes[currentMaxIndex]
        and currentMaxIndex == i and cntLeaders == 1):
            result += 1

    return result