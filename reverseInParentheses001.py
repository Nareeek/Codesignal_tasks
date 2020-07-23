def reverseInParentheses(s):
    while True:
        rightmost = s.find(")")
        
        if rightmost == -1:
            break
        
        leftmost = s[0: rightmost].rfind("(")
        
        start = s[0: leftmost]
        middle = s[leftmost + 1: rightmost][::-1]
        end = s[rightmost + 1: len(s)]
        
        s = start + middle + end
    
    return s
    
    
    '''
    def reverseInParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s
    '''
    
    '''
    def reverseInParentheses(inputString):
    stack = []
    for x in inputString:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop() # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)
    
    return "".join(stack)
    '''