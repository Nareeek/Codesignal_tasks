def addBinaryStrings(a, b):
    return bin(int(a or '0', 2) + int(b or '0', 2))[2:]
