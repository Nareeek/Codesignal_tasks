# 1
def isCorrectSentence(inputString):

    leadChar = inputString[0]
    endChar = inputString[len(inputString) - 1]

    if ('A' <= leadChar and leadChar <= 'Z'
          and endChar == '.'):
        return True
    else:
        return False
    
    
# 2
def isCorrectSentence(inputString):
    return all([inputString[0].isupper(), inputString[-1] == '.'])
    