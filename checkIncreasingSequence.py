def checkIncreasingSequence(seq):

    for i in range(1, len(seq)):
        if seq[i] <= seq[i - 1]:
            return False

    return True
