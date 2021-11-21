def combs(comb1, comb2):

    def getMask(comb):
        a = comb.replace('*', '1').replace('.', '0')
        return int(a, 2)

    m1 = getMask(comb1)
    m2 = getMask(comb2)
    len1 = len(comb1)
    len2 = len(comb2)
    answer = len1 + len2
    for i in range(-len1, len2 + 1):
        if i < 0:
            tmp = m2 << (-i) & m1
            length = max(-i + len2, len1)
        else:
            tmp = m1 << i & m2
            length = max(i + len1, len2)
        if tmp == 0 and answer > length:
            answer = length

    return answer