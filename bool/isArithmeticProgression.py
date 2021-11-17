def isArithmeticProgression(sequence):

    difference = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i - 1] != difference:
            return False
    return True