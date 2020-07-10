def doubleSwap(txt, ch1, ch2):
    str1 = ch1 + ch2
    str2 = ch2 + ch1

    nar = txt.maketrans(str1, str2)

    return txt.translate(nar)


print(doubleSwap("aabbccc", "a", "b"))

# bbaaccc
