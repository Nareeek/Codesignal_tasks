def insert(value: list, dic: dict):
    dic[value[0]] = value[1]
    return


def addToValue(value: list, dic: dict):
    digit = value[0]
    return {k: v + digit for (k, v) in dic.items()}


def addToKey(value: list, dic: dict):
    digit = value[0]
    return {k + digit: v for (k, v) in dic.items()}


def get(value: list, dic: dict):
    digit = value[0]
    return dic[digit]


def hashMap(queryType, query):
    d = {}
    get_sum = 0
    for i in range(len(queryType)):
        if queryType[i] == "insert":
            insert(query[i], d)
        elif queryType[i] == "addToValue":
            d = addToValue(query[i], d)
        elif queryType[i] == "addToKey":
            d = addToKey(query[i], d)
        elif queryType[i] == "get":
            get_sum += get(query[i], d)

    return get_sum


print(hashMap(["insert",
               "insert",
               "addToValue",
               "addToKey",
               "get"], [[1, 2],
                        [2, 3],
                        [2],
                        [1],
                        [3]]))
