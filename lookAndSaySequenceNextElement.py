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
