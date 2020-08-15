#1
def amendTheSentence(s):
    sentence = s[0].lower()
    
    for c in s[1:]:
        if c.isupper():
            sentence += " " + c.lower()                
        else:
            sentence += c            
    return sentence

# 2
def amendTheSentence(s):
    sentence = ""
    for i,c in enumerate(s):
        if c.isupper():
            if i!=0:
                sentence+=" "+c.lower()
            else:
                sentence+=c.lower()                  
        else:
            sentence+=c            
    return sentence


# 3
def amendTheSentence(s):
    s = list(s);
    a = []

    for i in range(len(s)):
        if s[i].isupper():
            a.append(i)
            s[i] = s[i].lower()

    ss = list(s)
    i = 0
    j = -1 if a[0] == 0 else 0

    while i < len(a):
        if a[i] != 0:
            ss.insert(a[i] + j, ".")
            j += 1;
            i += 1
        else:
            j += 1;
            i += 1

    return " ".join("".join(ss).split("."))


print(amendTheSentence("codesignalIsAwesome"))