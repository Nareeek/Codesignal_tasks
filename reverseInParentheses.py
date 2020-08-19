# 1
def reverseInParentheses(s):
    stack = []
    for x in s:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop()  # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)

    return "".join(stack)


print(reverseInParentheses("foo(bar(baz))blim"))


# 2
def reverseInParentheses(s):
    while True:
        right = s.find(")")

        if right == -1:
            break

        left = s[0: right].rfind("(")

        start = s[0: left]
        middle = s[left + 1: right][::-1]
        end = s[right + 1: len(s)]

        s = start + middle + end

    return s


print(reverseInParentheses("foo(bar(baz))blim"))


# 3-4
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