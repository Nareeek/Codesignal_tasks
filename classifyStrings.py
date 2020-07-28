def classifyStrings(s):
    if len(s) == 1:
        return "good"
    vowels = "aeiou"
    v = ""
    c = ""
    tmp1 = False
    tmp2 = False
    
    for x in (s + "-"):
        if x in vowels or x == "?":
            v += x
        else:
            if len(v) == 3:
                if "?" in v:
                    tmp1 = True
                else:
                    return "bad"
            v = "" 

    for x in (s + "-"):
        if (x not in vowels or x == "?") and x != "-":
            c += x
        else:
            if len(c) == 5:
                if "?" in c:
                    tmp2 = True
                else:
                    return "bad"
            c = ""
                
    if (tmp1 and tmp2) == True:
        return "bad"
    elif (not tmp1 and tmp2) or (not tmp2 and tmp1):
        return "mixed"
    return "good"



print(classifyStrings("typ?asdf?relkhfd"))

