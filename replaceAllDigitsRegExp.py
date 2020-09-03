def replaceAllDigitsRegExp(input):
    res = []
    for x in input:
        if x.isdigit():
            res.append("#")
        else:
            res.append(x)
            
    return ''.join(res)
            

