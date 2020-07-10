def additionWithoutCarrying(param1, param2):
    s = ""

    param1 = str(param1)
    param2 = str(param2)

    if len(param1) > len(param2):
        param2 = param2.zfill(len(param1))
    elif len(param2) > len(param1):
        param1 = param1.zfill(len(param2))
    
    for i in range(len(param1)):
        s += str((int(param1[i]) + int(param2[i])) % 10)
    
    return int(s)

print(additionWithoutCarrying(456, 1734))