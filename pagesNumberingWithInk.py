def pagesNumberingWithInk(current, numberOfDigits):
    while len(str(current)) <= numberOfDigits:
        numberOfDigits -= len(str(current))
        current += 1

    return current - 1


print(pagesNumberingWithInk(1, 5))
