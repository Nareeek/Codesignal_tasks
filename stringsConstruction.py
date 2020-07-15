# 1
def stringsConstruction(a, b):
    def counter(x):
        d = {}
        for el in x:
            d[el] = x.count(el)           
        return d
        
    a, b = counter(a), counter(b)
    l = []
    
    for k in a:
        try:
            l.append(b[k] // a[k])
        except:
            return 0
    return min(l)  


# 2
from collections import Counter

def stringsConstruction(a, b):
    a, b = Counter(a), Counter(b)
    l = []
    
    for k, v in a.items():
        l.append(b[k] // a[k])
    
    return min(l)

# 3
from collections import Counter as C


def stringsConstruction(a, b):
    return min(C(b)[k] // C(a)[k] for k in C(a))



print(stringsConstruction("za","bzc"))
print(stringsConstruction("zza","bzzzaaz"))
