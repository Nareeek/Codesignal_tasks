def killKthBit(n, k):
    return n & ~(1<<k-1)

print(killKthBit(374823748, 13))