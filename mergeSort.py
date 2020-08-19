# 1
def mergeSort(sequence):
    def merge(sequence, left, middle, right):

        result = []

        i = left
        j = middle
        while i < middle and j < right:
            if sequence[i] < sequence[j]:
                result.append(sequence[i])
                i += 1
            else:
                result.append(sequence[j])
                j += 1

        while i < middle:
            result.append(sequence[i])
            i += 1

        while j < right:
            result.append(sequence[j])
            j += 1

        for i in range(left, right):
            sequence[i] = result[i - left]

    def split(sequence, left, right):
        middle = (left + right) // 2

        if left + 1 == right:
            return
        split(sequence, left, middle)
        split(sequence, middle, right)
        merge(sequence, left, middle, right)

    split(sequence, 0, len(sequence))

    return sequence

# 2
def mergeStrings(s1, s2):
    itog = ""
    i = 0

    while i < (len(s1) + len(s2)):
        if len(s1) == 0:
            itog += s2[i:]
            return itog
        elif len(s2) == 0:
            itog += s1[i:]
            return itog

        if s1.count(s1[i]) < s2.count(s2[i]):
            itog += s1[i]
            s1 = s1[i + 1:]
        elif s2.count(s2[i]) < s1.count(s1[i]):
            itog += s2[i]
            s2 = s2[i + 1:]
        elif (s2.count(s2[i]) == s1.count(s1[i])) and (ord(s1[i]) != ord(s2[i])):
            if ord(s1[i]) < ord(s2[i]):
                itog += s1[i]
                s1 = s1[i + 1:]
            elif ord(s2[i]) < ord(s1[i]):
                itog += s2[i]
                s2 = s2[i + 1:]
        elif (s2.count(s2[i]) == s1.count(s1[i])) and (ord(s1[i]) == ord(s2[i])):
            itog += s1[i]
            s1 = s1[i + 1:]

    return itog


print(mergeStrings("super", "tower"))


# 3
def mergeStrings(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    t = []

    while len(s1) != 0 or len(s2) != 0:
        if len(s1) > 0 or len(s2) > 0:
            if s1.count(s1[0]) < s2.count(s2[0]):
                t.append(s1[0])
                s1.remove(s1[0])
            elif s1.count(s1[0]) > s2.count(s2[0]):
                t.append(s2[0])
                s2.remove(s2[0])
            else:
                if ord(s1[0]) <= ord(s2[0]):
                    t.append(s1[0])
                    s1.remove(s1[0])
                else:
                    t.append(s2[0])
                    s2.remove(s2[0])
        if len(s1) == 0:
            for i in range(len(s2)):
                t.append(s2[0])
            break
        elif len(s2) == 0:
            for i in range(len(s1)):
                t.append(s1[i])
            break
    t = "".join(t)
    return t


print(mergeStrings("ougtaleegvrabhugzyx", "wvieaqgaegbxg"))
