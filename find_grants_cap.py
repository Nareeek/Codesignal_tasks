def find_grants_cap(grantsArray, newBudget):
    d = {}
    s = 0

    for i in range(len(grantsArray)):
        if grantsArray[i] >= newBudget / len(grantsArray):
            d[i] = grantsArray[i]
        else:
            s += grantsArray[i]

    cap = float(float(newBudget) - float(s)) / float(len(d))

    dic = d.copy()

    for k, v in d.items():
        if v < cap:
            del dic[k]
            if len(dic) > 1:
                cap = newBudget / len(dic)
            elif len(dic) in [0, 1]:
                return newBudget - (sum(grantsArray) - v)
    return cap if len(dic) != 1 else newBudget - (sum(grantsArray) - v)


print(find_grants_cap([210, 200, 150, 193, 130, 110, 209, 342, 117], 1530))
