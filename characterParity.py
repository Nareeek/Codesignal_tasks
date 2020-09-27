def characterParity(symbol):
    if symbol.isdigit():
        if int(symbol) % 2 == 0:
            return 'even'
        else:
            return 'odd'
    return 'not a digit'

