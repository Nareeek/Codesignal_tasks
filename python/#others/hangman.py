def hangman(word, letters):
    c = 0
    d = {}
    for i in list(word):
        d[i] = 1
    print d
    for i in letters:
        print d
        if i in d:
            d.pop(i)
        else:
            c+=1
        if c == 6 and len(d.keys()) > 0:
            return False
    if len(d.keys()) > 0:
        return False
    return True