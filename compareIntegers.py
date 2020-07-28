def compareIntegers(a, b):

    if len(a) > len(b):
        return 'greater'
    if len(a) < len(b):
        return 'less'
    if a < b:
        return 'less'
    if a > b:
        return "greater"
    return 'equal'