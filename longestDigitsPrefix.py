def longestDigitsPrefix(inputString):
    s = ""
    for x in inputString:
        if x.isdigit():
            s += x
        else:
            return s
    return s
print(longestDigitsPrefix("0123456789"))