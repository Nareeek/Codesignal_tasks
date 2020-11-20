def makeArrayConsecutive2(sequence):
    a = min(sequence)
    b = max(sequence)
    L = []
    while a < b:
        if a + 1 not in sequence:
            L.append(a + 1)
        a += 1
    return L



# 2
def makeArrayConsecutive2(sequence):
    M = max(sequence)
    m = min(sequence)
    res = []
    for i in range(m, M):
        if i not in sequence:
            res.append(i)
    return res


# 3
def makeArrayConsecutive2(statues):

    current_position = 0
    answer = 0

    statues.sort()
    for i in range(min(statues), max(statues)+1):
        if statues[current_position] != i:
            answer += 1
        else:
            current_position += 1

    return answer