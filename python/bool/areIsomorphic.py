def areIsomorphic(array1, array2):
    l1 = [len(i) for i in array1]
    l2 = [len(i) for i in array2]
    if len(array1) == len(array2) and l1 == l2:
        return True
    return False
        