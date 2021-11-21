def countVowelConsonant(s):
    vowels = 'aeiou'
    summ = 0
    for x in s:
        if x in vowels:
            summ += 1
        else:
            summ += 2
    return summ
    

