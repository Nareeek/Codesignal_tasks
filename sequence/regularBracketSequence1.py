# 1
def regularBracketSequence1(sequence):

    balance = 0
    for i in range(len(sequence)):
        if sequence[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    if balance > 0:
        return False
    return True



# 2
def regularBracketSequence1(sequence):
    cnt = 0
    for i in sequence:
        if i == "(":
            cnt +=1
        elif i==")":
            cnt -=1
        if cnt <0:
            return False
    return cnt ==0