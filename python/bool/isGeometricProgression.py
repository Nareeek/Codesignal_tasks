def isGeometricProgression(sequence):
    d = sequence[1] / sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] / sequence[i - 1] != d:
            return False
    return True
