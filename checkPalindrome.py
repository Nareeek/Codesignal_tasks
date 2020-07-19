def checkPalindrome(inputString):

    isPalindrome = True
    for i in range(len(inputString)):
        if inputString[i] != inputString[len(inputString) - i - 1]:
            isPalindrome = False
            break

    return isPalindrome