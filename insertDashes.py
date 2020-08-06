def insertDashes(inputString):
    inp = inputString
    
    if len(inp) < 2:
        return inp
    
    i = 1
    while i < len(inp):
        if inp[i - 1].isalpha() and inp[i].isalpha():
            inp = inp[0: i] + '-' + inp[i: len(inp)]
        i += 1
    
    return inp