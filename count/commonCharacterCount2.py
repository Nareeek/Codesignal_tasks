def commonCharacterCount2(s):
    setsOfCharacters = map(set, s)
    commonCharacters = functools.reduce(set.intersection, setsOfCharacters)

    count = 0

    for character in commonCharacters:
        count += min(map(lambda x: x.count(character), s))

    return count
