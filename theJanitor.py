def theJanitor(word):
    z = [0]*26
    for i in set(word):
        z[ord(i)-97] = len(word)-word.index(i)-word[::-1].index(i)
        
    return z 