# 1
def containsDuplicates(a):
    return len(set(a)) < len(a)

# 2
def containsDuplicates(a):
    for i in a:
        if a.count(i) >1:
            return True
    return False
