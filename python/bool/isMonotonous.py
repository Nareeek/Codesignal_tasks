def isMonotonous(sequence):
    if len(sequence) == 1:
        return True
    direction = sequence[1] - sequence[0]
    for i in range(0, len(sequence) - 1):
        if direction * (sequence[i + 1] - sequence[i]) <= 0:
            return False
    return True