def generateParentheses(n):
    result = []
    generateParenthesisUtil(n, n, "", result)
    return result
def generateParenthesisUtil(left, right, temp, result):
    if left == 0 and right == 0:
        result.append(temp)
        return
    if left > 0:
        generateParenthesisUtil(left - 1, right, temp + '(', result)
    if right > left:
        generateParenthesisUtil(left, right - 1, temp + ')', result)