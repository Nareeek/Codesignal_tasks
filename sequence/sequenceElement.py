# 1
def sequenceElement(a, n):

    MOD = 10**5
    seq = []
    for i in range(5):
        seq.append(a[i])

    lastFive = (a[0] * 10**4 + a[1] * 10**3 +
                a[2] * 10**2 + a[3] * 10**1 + a[4])
    was = {}
    was[lastFive] = 4

    i = 5
    while True:
        seq.append((seq[i - 1] + seq[i - 2] +
                    seq[i - 3] + seq[i - 4] + seq[i - 5]) % 10)
        lastFive = (lastFive * 10 + seq[i]) % MOD
        if lastFive in was:
            last = was[lastFive]
            return seq[n % (i - last)]
        else:
            was[lastFive] = i
        i += 1
        
        
# 2
def sequenceElement(a, n):
    if len(a) - 1 >= n:
        return a[n]
    tmp = ''.join(str(v) for v in a)
    cnt = 0
    # it is easy to prove that 4686 is the first position
    # the sequence is repeated
    while cnt < 4686:
        cnt += 1
        i = len(a)
        curr = (a[i - 5] + a[i - 4] + a[i - 3] + a[i - 2] + a[i - 1]) % 10
        a.append(curr)

    loop = ''.join(str(v) for v in a)[:4686]
    # print(loop)
    return int(loop[n % (len(loop))])

