def capitalizeVowelsRegExp(input):
    v = "aeiouy"
    inp = list(input)
    for i in range(len(inp)):
        if inp[i] in v and inp[i].islower():
            inp[i] = inp[i].upper()
            
    return "".join(inp)