def permute(list, s):
    if list == 1:

        return s

    else:

        List = []

        for y in permute(1, s):

            for x in permute(list - 1, s):
                List.append((y + x))

    return List


# print(permute(1, ["a","b","c"]))
print(permute(3, ["a", "b", "c"]))
