# 1
def isDigit(symbol):

    if symbol.isdigit():
        return True
    return False


# 2

def isDigit(symbol):

    if '0' <= symbol and symbol <= '9':
        return True
    return False

# 3
def firstDigit(inputString):

    return re.search('[0-9]', inputString).group(0)
