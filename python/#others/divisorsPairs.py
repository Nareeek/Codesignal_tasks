def divisorsPairs(sequence):
    result = 0

    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] % sequence[j] == 0 or sequence[j] % sequence[i] == 0:
                result += 1

    return result
