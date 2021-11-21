def latinLettersSearchRegExp(s):
    v = 'azertyuiopmlkjhgfdsqwxcvbn'
    for e in s:
        if e.lower() in v:
            return True
    return False
    

