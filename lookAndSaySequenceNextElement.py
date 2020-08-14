def lookAndSaySequenceNextElement(element):
    l = element[0]
    element += ' '
    c = 1
    o = ''
    for e in element[1:]:
        if l != e:
            o += str(c) + l
            l = e
            c = 1
        else:
            c += 1
    return o


# 2
def lookAndSaySequenceNextElement(element):
    count = 1
    res = ""
    currentEle = element[0]
    for i in range(1, len(element)):
        if element[i] == element[i - 1]:
            count += 1
        else:
            res += str(count) + currentEle
            count = 1
            currentEle = element[i]
            
    res += str(count) + currentEle
    
    return res
