def hashMap(queryType, query):
    a = []
    get = 0

    for (i, j) in zip(queryType, query):

        if i == "insert":
            if j[0] < 0 and abs(j[0]) > len(a):
                a = [0] * ((-j[0]) - len(a)) + a
                a[j[0]] = j[1]

            elif j[0] <= len(a):
                a.insert(j[0], j[1])
            elif j[0] >= 0:
                a = [0] * j[0] + a
                a[j[0]] = j[1]

        elif i == "addToKey":
            if j[0] >= 0:
                a = [0] * j[0] + a
            else:
                a = a[-j[0]:] + a[:-j[0]]

        elif i == "addToValue":
            a = list(map(lambda x: x + j[0], a))

        elif i == "get":
            if j[0] < 0:
                if abs(j[0]) < len(a):
                    get += a[j[0]]
            elif j[0] <= len(a):
                get += a[j[0]]

    return get


print(hashMap(["addToValue",
               "addToValue",
               "insert",
               "insert",
               "insert",
               "addToValue",
               "addToValue",
               "addToKey",
               "get",
               "addToKey",
               "insert",
               "addToKey",
               "addToKey",
               "insert",
               "get",
               "addToValue",
               "addToValue",
               "insert",
               "get",
               "addToValue",
               "addToKey",
               "addToValue",
               "addToValue",
               "get",
               "insert",
               "insert",
               "get",
               "get",
               "get",
               "addToValue",
               "addToKey",
               "addToKey",
               "insert",
               "addToKey",
               "insert",
               "get",
               "get",
               "get",
               "addToKey",
               "insert",
               "addToValue",
               "addToValue",
               "get",
               "addToKey",
               "get",
               "get",
               "addToValue",
               "addToValue",
               "addToValue",
               "insert",
               "addToValue",
               "addToKey",
               "insert",
               "addToValue",
               "get",
               "addToKey",
               "insert",
               "addToValue",
               "addToValue",
               "addToValue",
               "addToValue",
               "get",
               "get",
               "addToKey",
               "insert",
               "insert",
               "addToKey",
               "addToValue",
               "addToKey",
               "addToKey",
               "insert",
               "get",
               "addToValue",
               "addToKey",
               "insert",
               "addToKey",
               "get",
               "get",
               "addToValue",
               "addToValue",
               "get",
               "insert",
               "insert",
               "addToKey",
               "addToValue",
               "insert",
               "addToKey",
               "insert",
               "addToKey",
               "insert",
               "addToKey",
               "addToKey",
               "get",
               "insert",
               "insert",
               "addToValue",
               "get",
               "get",
               "addToValue",
               "addToValue"],
              [[-10],
               [-32],
               [-37, 32],
               [-45, 26],
               [-25, -23],
               [23],
               [49],
               [-14],
               [-39],
               [15],
               [3, 44],
               [3],
               [-35],
               [40, 22],
               [-56],
               [-34],
               [38],
               [6, -39],
               [-29],
               [1],
               [43],
               [-30],
               [37],
               [-33],
               [-23, 45],
               [-48, -21],
               [-23],
               [49],
               [14],
               [3],
               [28],
               [-29],
               [38, 11],
               [-46],
               [20, 20],
               [-95],
               [-33],
               [-70],
               [-19],
               [-14, 36],
               [16],
               [-42],
               [-79],
               [20],
               [3],
               [6],
               [36],
               [-32],
               [24],
               [7, -12],
               [34],
               [-33],
               [-46, 1],
               [-14],
               [-26],
               [35],
               [-21, -48],
               [-2],
               [-1],
               [41],
               [7],
               [5],
               [-69],
               [5],
               [-40, 33],
               [-48, -20],
               [38],
               [49],
               [48],
               [40],
               [-14, -9],
               [39],
               [42],
               [-25],
               [48, 34],
               [-41],
               [88],
               [-4],
               [-47],
               [-23]]))
