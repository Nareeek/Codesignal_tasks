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
