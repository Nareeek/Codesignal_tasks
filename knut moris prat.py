def findFirstSubstringOccurrence(s, x):
    ''' Find the first occurrances of @patt in @text
    '''
    patt = x
    text = s
    if not patt or not text: 
        return -1

    # First build the pattern lookup table
    tbl = [0] * (1 + len(patt))
    i = 1; j = 0;
    while i < len(patt):
        if patt[i] == patt[j]:
            i += 1; j += 1; tbl[i] = j
        elif 0 == j:
            i += 1
        else:
            j = tbl[j]

    
    # Search over the query text
    i = 0; j = 0;
    while i < len(text):
        if text[i] == patt[j]:
            i += 1; j += 1;
            if len(patt) == j:
                assert(text[i - len(patt): i] == patt)
                return i - len(patt)
        elif j == 0:
            i += 1
        else:
            j = tbl[j]

    return -1

print(findFirstSubstringOccurrence("CodefightsIssAwesome", "IssA"))